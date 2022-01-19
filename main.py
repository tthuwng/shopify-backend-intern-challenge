from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn

@app.route("/")
def index():
  conn = get_db_connection()
  inventories = conn.execute('SELECT * FROM inventories').fetchall()
  print(inventories)
  conn.close()
  return render_template('index.html', inventories=inventories)
