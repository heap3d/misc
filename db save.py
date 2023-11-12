#!/usr/bin/python
import sqlite3

conn = sqlite3.connect(r"D:\work\scripts\modo\h3d tools\misc\people.db")

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER, first_name TEXT, last_name TEXT)')
conn.commit()

names_list = (
    (1, "Roderick", "Watson"),
    (2, "Roger", "Hom"),
    (3, "Petri", "Halonen"),
    (4, "Jussi", ""),
    (5, "Janes", "McCann")
)

cur.executemany('INSERT INTO people (id, first_name, last_name) VALUES (?,?,?)', names_list)
conn.commit()

cur.close()
conn.close()

