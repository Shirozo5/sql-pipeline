# Best selling products by revenue and quantity sold

import sqlite3
import pandas as pd
import os


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 30)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'northwind.sqlite')

conn = sqlite3.connect(db_path)
dq_path= os.path.join(BASE_DIR, 'q3_best_products.sql')
with open(dq_path) as f:
    query = f.read()

df = pd.read_sql_query(query, conn)
print(df.to_markdown(index=False))
