import os
import pandas as pd
from products_load import ProductLoader
from snowflake_connection import connect_to_snowflake

conn = connect_to_snowflake.get_connection()

file = os.path.expanduser("~/Projects/retail-sales-analytics-pipeline/data/products.json")
schema = os.path.expanduser("~/Projects/retail-sales-analytics-pipeline/config/schema_products.json")

try:
    loader = ProductLoader(conn)
    loader.validate_and_load_products_file(file, schema, conn, "LND_PRODUCTS", "RETAIL_LANDING")
except Exception as e:
    print(e)

conn.close()