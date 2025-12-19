#!/bin/bash

set -e

echo "Generating debezium connector configuration"

# Check if template exists
if [ ! -f "src/config/debezium-mysql-connector.template.json" ]; then
    echo "Error: Template file not found."
    exit 1
fi

# Set values
MYSQL_HOST=${MYSQL_HOST:-mysql-source}
MYSQL_PORT=${MYSQL_PORT:-3306}
MYSQL_USER=${MYSQL_USER:-dbuser}
MYSQL_PASSWORD=${MYSQL_PASSWORD:-dbpassword}
MYSQL_DATABASE=${MYSQL_DATABASE:-orders_db}

# Generate the config file
sed -e "s/MYSQL_HOST_PLACEHOLDER/$MYSQL_HOST/g" \
    -e "s/MYSQL_PORT_PLACEHOLDER/$MYSQL_PORT/g" \
    -e "s/MYSQL_USER_PLACEHOLDER/$MYSQL_USER/g" \
    -e "s/MYSQL_PASSWORD_PLACEHOLDER/$MYSQL_PASSWORD/g" \
    -e "s/MYSQL_DATABASE_PLACEHOLDER/$MYSQL_DATABASE/g" \
    src/config/debezium-mysql-connector.template.json > src/config/debezium-mysql-connector.json

echo "Configuration file generated in src/config/debezium-mysql-connector.json"

