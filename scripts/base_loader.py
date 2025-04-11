import os
import pandas as pd
import json

class BaseLoader:
    def __init__(self):
        print("Initialized parent")

    def load_file(self, data_file, schema_file):
        self.data_file = data_file
        self.schema_file = schema_file

        json_data = pd.read_json(self.data_file)
        df = pd.DataFrame(json_data)
        
        with open(self.schema_file, 'r') as f:
            schema = json.load(f)
            
        try:
            df = df.astype(schema)
        except Exception as e:
            print(f"Data doesnt confirm to schema: {e}")

        return df
        
    def insert_into_snowflake(self, connector, df):
        self.conn = connector
        self.df = df
        
        print(self.conn)
        print(self.df.head(3))