#!/usr/bin/env python3

import os
import sys
import time
import random
from datetime import datetime
from typing import Optional
import mysql.connector
from mysql.connector import Error
from faker import Faker
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'port': int(os.getenv('MYSQL_PORT', 3306)),
    'user': os.getenv('MYSQL_USER', 'dbuser'),
    'password': os.getenv('MYSQL_PASSWORD', 'dbpassword'),
    'database': os.getenv('MYSQL_DATABASE', 'orders_db'),
}

INSERT_RATE = int(3)
UPDATE_RATE = int(5)
DELETE_RATE = int(1)
INTERVAL_SECONDS = int(5)

fake = Faker()

CATEGORIES = {
    'Electronics': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headset', 'Speaker', 'Tablet'],
    'Furniture': ['Chair', 'Desk', 'Lamp', 'Bookshelf', 'Cabinet'],
    'Office': ['Notebook', 'Pen', 'Pencil', 'Stapler', 'Folder', 'Binder'],
    'Kitchen': ['Mug', 'Bottle', 'Lunch Box', 'Cutlery', 'Plate'],
    'Books': ['Programming', 'Design', 'Management', 'Marketing', 'Finance'],
}


class ProductGenerator:
    """Products generator"""
    
    def __init__(self, connection):
        self.conn = connection
    
    def add_product(self) -> bool:
        """Add a new product"""
        try:
            category = random.choice(list(CATEGORIES.keys()))
            product_type = random.choice(CATEGORIES[category])
            
            # name
            if category == 'Books':
                name = f"{product_type} {random.choice(['Basics', 'Advanced', 'Guide', 'Handbook'])}"
            else:
                name = f"{product_type} {random.choice(['Pro', 'Plus', 'Lite', 'Premium', 'Standard'])}"
            
            # price
            price_ranges = {
                'Electronics': (19.99, 999.99),
                'Furniture': (49.99, 499.99),
                'Office': (2.99, 29.99),
                'Kitchen': (5.99, 39.99),
                'Books': (19.99, 59.99),
            }
            min_price, max_price = price_ranges[category]
            price = round(random.uniform(min_price, max_price), 2)
            
            # stock
            stock = random.randint(10, 500)
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO products (name, category, price, stock, status)
                VALUES (%s, %s, %s, %s, 'active')
            """, (name, category, price, stock))
            
            self.conn.commit()
            product_id = cursor.lastrowid
            cursor.close()
            
            print(f"Product: {name}, ${price}, Stock: {stock}")
            return True
            
        except Error as e:
            print(f"Error inserting product: {e}")
            self.conn.rollback()
            return False
    
    def update_price(self) -> bool:
        """Update product"""
        try:
            cursor = self.conn.cursor()
            
            # Get a random product
            cursor.execute("""
                SELECT product_id, name, price
                FROM products
                WHERE status = 'active'
                ORDER BY RAND()
                LIMIT 1
            """)
            
            result = cursor.fetchone()
            if not result:
                cursor.close()
                return False
            
            product_id, name, old_price = result
            
            change = random.uniform(-0.20, 0.20)
            new_price = round(max(0.99, float(old_price) * (1 + change)), 2)
            
            cursor.execute("""
                UPDATE products
                SET price = %s
                WHERE product_id = %s
            """, (new_price, product_id))
            
            self.conn.commit()
            cursor.close()
            
            print(f"Price: {name} changed from ${old_price:.2f} to ${new_price:.2f}")
            return True
            
        except Error as e:
            print(f"Error updating price: {e}")
            self.conn.rollback()
            return False
    
    def delete_old_product(self) -> bool:
        """Delete product"""
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT product_id, name
                FROM products
                WHERE status = 'discontinued'
                AND updated_at < DATE_SUB(NOW(), INTERVAL 30 MINUTE)
                ORDER BY RAND()
                LIMIT 1
            """)
            
            result = cursor.fetchone()
            if not result:
                cursor.close()
                return False
            
            product_id, name = result
            
            cursor.execute("""
                DELETE FROM products
                WHERE product_id = %s
            """, (product_id,))
            
            self.conn.commit()
            cursor.close()
            
            print(f"Deleted: {name}")
            return True
            
        except Error as e:
            print(f"Error deleting product: {e}")
            self.conn.rollback()
            return False


def get_db_connection():
    """DB connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print(f"Connected to MySQL: {DB_CONFIG['database']}")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def main():
    """Main loop"""
    
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to DB. Exiting.")
        sys.exit(1)
    
    generator = ProductGenerator(conn)
    cycle = 0
    try:
        while True:
            cycle += 1
            
            # New products
            for _ in range(INSERT_RATE):
                generator.add_product()
                time.sleep(0.2)
            
            # Update prices
            for _ in range(UPDATE_RATE // 2):
                generator.update_price()
                time.sleep(0.2)
            
            # Delete product
            for _ in range(DELETE_RATE):
                generator.delete_old_product()
                time.sleep(0.2)
            
            print(f"\nWaiting {INTERVAL_SECONDS}s...\n")
            time.sleep(INTERVAL_SECONDS)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
