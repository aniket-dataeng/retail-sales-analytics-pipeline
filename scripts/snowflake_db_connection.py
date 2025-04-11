import os
from dotenv import load_dotenv
from snowflake import connector

load_dotenv(dotenv_path=os.path.expanduser("~/Projects/retail-sales-analytics-pipeline/config/snowflake.env"),  override=True)

try:
    conn = connector.connect(
        user=os.getenv("SF_USER"),
        password=os.getenv("SF_PASSWORD"),
        account=os.getenv("SF_ACCOUNT"),
        warehouse=os.getenv("SF_WAREHOUSE"),
        database=os.getenv("SF_DATABASE"),
        schema=os.getenv("SF_SCHEMA"),
        role=os.getenv("SF_ROLE")
    )
    print(f"Snowflake Connection Successful")
    cur = conn.cursor()
except Exception as e:
    print(f"Could not connect to snowflake: {e}")

def insert_products

#cur.execute("select Table_name from information_schema.tables where table_name like 'LND%';")
#for i in cur.fetchall():
#    print(i[0])

cur.close()
conn.close()
print(f"Snowflake Connection Closed")
