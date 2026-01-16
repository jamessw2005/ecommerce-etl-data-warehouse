CREATE TABLE dim_customers (
    customer_id VARCHAR PRIMARY KEY,
    city VARCHAR,
    state VARCHAR
);

CREATE TABLE dim_products (
    product_id VARCHAR PRIMARY KEY,
    category VARCHAR,
    weight FLOAT
);

CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

CREATE TABLE fact_sales (
    order_id VARCHAR,
    customer_id VARCHAR,
    product_id VARCHAR,
    date_id DATE,
    price FLOAT,
    payment_value FLOAT
);

