#!/usr/bin/python
import sqlite3

conn = sqlite3.connect(r"D:\work\scripts\modo\h3d tools\misc\people.db")

cur = conn.cursor()

# cur.execute('SELECT * FROM people ORDER BY last_name')
# data = cur.fetchall()

user_input = "' OR 1=1 --"
user_input = "1"

sql = f"SELECT * FROM people WHERE id = '{user_input}'"
# data_read = cur.execute(sql)
data_read = cur.execute("SELECT * FROM people WHERE id=(?)", user_input)

# for row in data:
#     print(row)

for row in data_read:
    print(row)
    
cur.close()
conn.close()