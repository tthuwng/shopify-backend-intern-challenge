import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO inventories (name, description) VALUES (?,?)",("First Item", "Description for the first item"))

cur.execute("INSERT INTO inventories (name, description) VALUES (?,?)",("Second Item", "Description for the second item"))

connection.commit()
connection.close()

