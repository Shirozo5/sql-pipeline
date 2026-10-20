# top ten customers by revenue

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
dq_path = os.path.join(BASE_DIR, 'q1_top_customers.sql')
with open(dq_path) as f:
    query = f.read()

df = pd.read_sql_query(query, conn)

# Create a horizontal bar chart
df = df.sort_values('Revenue')  # ascending so biggest bar ends up on top
plt.figure(figsize=(10, 6))
plt.barh(df['CompanyName'], df['Revenue'], color='#4C72B0')
plt.xlabel('Revenue ($)')
plt.title('Top 10 Customers by Revenue')
plt.tight_layout()
plt.savefig('q1_top_customers.png', dpi=150)
plt.show()