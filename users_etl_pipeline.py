import requests
import pandas as pd
import sqlite3

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)
data = r.json()

# Flatten nested JSON properly
df = pd.json_normalize(data)

# Keep only useful columns for interview
df_small = df[['id', 'name', 'email', 'address.city', 'phone']].copy()
df_small.columns = ['id', 'name', 'email', 'city', 'phone']

conn = sqlite3.connect("users.db")
df_small.to_sql("users", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT * FROM users WHERE city LIKE 'S%'", conn)
print(result[['name','city']])
print(f"Count: {len(result)}")