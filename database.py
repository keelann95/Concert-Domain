
import sqlite3

def connect_db():
    conn = sqlite3.connect('concerts.db')  # Create or connect to the database
    return conn
