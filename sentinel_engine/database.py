# database.py
import sqlite3
import pandas as pd
from config import DB_PATH

def get_connection():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def fetch_transactions():
    conn = get_connection()
    if conn:
        df = pd.read_sql_query("SELECT * FROM ledger ORDER BY user_id, timestamp ASC", conn)
        conn.close()
        return df
    return pd.DataFrame()