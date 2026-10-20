# Monthly Sales Trends.

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
dq_path= os.path.join(BASE_DIR, 'q2_monthly_sales.sql')
with open(dq_path) as f:
    query = f.read()

df = pd.read_sql_query(query, conn)
print(df.to_markdown(index=False))

# Chart
plt.figure(figsize=(12, 5))
plt.plot(df['Month'], df['Revenue'], marker='o', color='#DD8452')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q2_monthly_sales.png', dpi=150)
plt.show()