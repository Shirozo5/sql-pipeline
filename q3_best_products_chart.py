# Best selling products by revenue and quantity sold

import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 30)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'northwind.sqlite')

conn = sqlite3.connect(db_path)
dq_path = os.path.join(BASE_DIR, 'q3_best_products.sql')
with open(dq_path) as f:
    query = f.read()

df = pd.read_sql_query(query, conn)

print(df.to_markdown(index=False))

# Chart
top10 = df.nlargest(10, 'Revenue')

plt.figure(figsize=(10, 6))
plt.bar(top10['Product Name'], top10['Revenue'], color='#55A868')
plt.xticks(rotation=60, ha='right')
plt.ylabel('Revenue ($)')
plt.title('Top 10 Best-Selling Products')
plt.tight_layout()

# Save the figure before showing it
plt.savefig(os.path.join(BASE_DIR, 'q3_best_products.png'), dpi=150)
plt.show()