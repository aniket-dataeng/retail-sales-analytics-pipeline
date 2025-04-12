import os
import json
import pandas as pd
import snowflake.connector
from base_loader import BaseLoader

class ProductLoader(BaseLoader):
    def __init__(self, connector):
        self.conn = connector

    def validate_and_load_products_file(self, data_file, schema_file, connector, table, schema):
        self.table = table
        self.schema = schema_file
        try:
            loader = BaseLoader()
            df = loader.load_file(data_file, schema_file)
            loader.insert_into_snowflake(connector, df, table, schema)
        except Exception as e:
            print(f"Error {e}")
        