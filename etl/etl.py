import pandas as pd
import psycopg2

# ---------- Load CSV files ----------
customers = pd.read_csv("data/olist_customers_dataset.csv")
orders = pd.read_csv("data/olist_orders_dataset.csv")
items = pd.read_csv("data/olist_order_items_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")

# ---------- Transform ----------
sales = (
    orders
    .merge(items, on="order_id")
    .merge(payments, on="order_id")
    .merge(customers, on="customer_id")
    .merge(products, on="product_id")
)

sales['order_purchase_timestamp'] = pd.to_datetime(
    sales['order_purchase_timestamp']
)
sales['date_id'] = sales['order_purchase_timestamp'].dt.date

# ---------- PostgreSQL connection ----------
conn = psycopg2.connect(
    host="localhost",
    database="ecomdb",
    user="postgres",
    password="YOUR_PASSWORD"
)

cur = conn.cursor()

# ---------- Load dim_customers ----------
for _, r in sales[['customer_id','customer_city','customer_state']].drop_duplicates().iterrows():
    cur.execute("""
        INSERT INTO dim_customers (customer_id, city, state)
        VALUES (%s,%s,%s)
        ON CONFLICT DO NOTHING
    """, (r.customer_id, r.customer_city, r.customer_state))

# ---------- Load dim_products ----------
for _, r in sales[['product_id','product_category_name','product_weight_g']].drop_duplicates().iterrows():
    cur.execute("""
        INSERT INTO dim_products (product_id, category, weight)
        VALUES (%s,%s,%s)
        ON CONFLICT DO NOTHING
    """, (r.product_id, r.product_category_name, r.product_weight_g))

# ---------- Load dim_date ----------
for d in sales['date_id'].unique():
    cur.execute("""
        INSERT INTO dim_date (date_id, year, month, day)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT DO NOTHING
    """, (d, d.year, d.month, d.day))

# ---------- Load fact_sales ----------
for _, r in sales.iterrows():
    cur.execute("""
        INSERT INTO fact_sales
        (order_id, customer_id, product_id, date_id, price, payment_value)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (r.order_id, r.customer_id, r.product_id,
          r.date_id, r.price, r.payment_value))

conn.commit()
cur.close()
conn.close()

print("✅ ETL COMPLETED SUCCESSFULLY")

