CREATE OR REPLACE SCHEMA RETAIL_LANDING;

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_PRODUCTS (
    "product_id" STRING,
    "product_name" STRING,
    "category" STRING,
    "price" FLOAT,
    "quantity" INT,
    "ingest_ts" TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_CUSTOMERS (
    customer_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    phone STRING,
    address STRING,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_ORDERS (
    order_id STRING,
    customer_id STRING,
    order_date DATE,
    store_id STRING,
    employee_id STRING,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_ORDER_ITEMS (
    order_item_id STRING,
    order_id STRING,
    product_id STRING,
    quantity INT,
    price FLOAT,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_CATEGORIES (
    category_id STRING,
    category_name STRING,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_STORES (
    store_id STRING,
    store_name STRING,
    location STRING,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_EMPLOYEES (
    employee_id STRING,
    first_name STRING,
    last_name STRING,
    title STRING,
    store_id STRING,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_LANDING.LND_INVENTORY (
    inventory_id STRING,
    product_id STRING,
    store_id STRING,
    stock_quantity INT,
    last_updated DATE,
    ingest_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE RETAIL_TARGET.SALES_ANALYTICS (
    order_id STRING,
    order_date DATE,
    
    -- Customer info
    customer_id STRING,
    customer_name STRING,
    email STRING,
    phone STRING,
    address STRING,
    
    -- Product info
    product_id STRING,
    product_name STRING,
    category_id STRING,
    category_name STRING,
    product_price FLOAT,
    quantity INT,
    
    -- Store info
    store_id STRING,
    store_name STRING,
    store_location STRING,
    
    -- Employee info
    employee_id STRING,
    employee_name STRING,
    employee_title STRING,

    -- Derived fields
    order_item_total FLOAT,
    ingest_ts TIMESTAMP
);


