🚀 End-to-End Data Engineering Project

# E-Commerce Sales Analytics ETL Pipeline

📌 Overview
This project implements an end-to-end ETL pipeline that transforms raw e-commerce transactional data into an analytics-ready data warehouse and visualizes insights using a BI dashboard.

---

## 🏗 Architecture
Raw CSV Data → Python (ETL) → PostgreSQL (Data Warehouse) → Power BI Dashboard

---

## 🔄 ETL Process
- Extract data from raw CSV files
- Transform data using Python (joins, date processing)
- Load cleaned data into PostgreSQL using a star schema

---

## 🗂 Data Warehouse Schema
**Fact Table**
- fact_sales

**Dimension Tables**
- dim_customers
- dim_products
- dim_date

---

## 🧰 Tech Stack
- Python (pandas, psycopg2)
- PostgreSQL
- SQL
- Power BI

---

# 📊 Dashboard Insights
- Total revenue
- Monthly sales trend
- Top product categories
- Sales by city


🚀 How to Run
1. Create PostgreSQL database `ecomdb`
2. Run `schema.sql`
3. Set DB password as environment variable
4. Execute `etl.py`
5. Open Power BI and connect to PostgreSQL


## 📌 Key Learnings
- ETL pipeline development
- Data warehouse modeling
- OLAP analytics
- BI dashboard creation
