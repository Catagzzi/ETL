USE orders_db;

INSERT INTO products (name, category, price, stock, status) VALUES
('Laptop Pro 15"', 'Electronics', 1299.99, 25, 'active'),
('Wireless Mouse', 'Electronics', 29.99, 150, 'active'),
('USB-C Cable', 'Electronics', 12.99, 200, 'active'),
('Mechanical Keyboard', 'Electronics', 89.99, 75, 'active'),
('4K Monitor 27"', 'Electronics', 399.99, 30, 'active'),
('Webcam HD', 'Electronics', 69.99, 100, 'active'),

('Ergonomic Desk Chair', 'Furniture', 249.99, 20, 'active'),
('Standing Desk', 'Furniture', 449.99, 15, 'active'),
('Desk Lamp LED', 'Furniture', 34.99, 80, 'active'),

('Notebook A5', 'Office', 4.99, 500, 'active'),
('Pen Set (10pcs)', 'Office', 9.99, 300, 'active'),
('Sticky Notes Pack', 'Office', 6.99, 400, 'active'),

('Coffee Mug', 'Kitchen', 9.99, 200, 'active'),
('Water Bottle', 'Kitchen', 14.99, 150, 'active'),
('Lunch Box', 'Kitchen', 19.99, 100, 'active'),

('Python Programming', 'Books', 39.99, 50, 'active'),
('Data Engineering Guide', 'Books', 44.99, 40, 'active'),
('SQL Cookbook', 'Books', 34.99, 60, 'active'),

('Old Mouse Model', 'Electronics', 19.99, 5, 'discontinued'),
('Legacy Keyboard', 'Electronics', 49.99, 2, 'discontinued');

