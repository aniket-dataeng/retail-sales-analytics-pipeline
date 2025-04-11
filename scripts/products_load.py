import os
import json
import pandas as pd

data_file = os.path.expanduser("~/Projects/retail-sales-analytics-pipeline/data/products.json")
schema_file = os.path.expanduser("~/Projects/retail-sales-analytics-pipeline/config/schema_products.json")

json_data = pd.read_json(data_file)
df = pd.DataFrame(json_data)

with (schema_file) as f:
    schema = json.load(f)

try:
    df = df.astype(schema)
except Exception e:
    print(f"Data doesnt confirm to schema: {e}")