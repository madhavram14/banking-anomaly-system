import sqlite3
import pandas as pd
from config import DB_PATH

def ingest_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"📡 System Path Locked: {DB_PATH}")

    # 1. Manually create the table with Constraints
    # This ensures we have a Primary Key and no negative amounts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ledger (
            txn_id TEXT PRIMARY KEY, 
            user_tier TEXT NOT NULL,
            amount_inr REAL NOT NULL CHECK(amount_inr > 0),
            city TEXT DEFAULT 'UNKNOWN',
            status TEXT,
            timestamp DATETIME NOT NULL
        )
    """)
    
    # 2. Add an Index for performance (Day 11 optimization)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_timestamp ON ledger(timestamp);")

    # 3. Load the CSV
    df = pd.read_csv('day2_transactions.csv')
    
    # 4. Use 'append' instead of 'replace' 
    # Because 'replace' would delete our hard work above!
    # We clear the data manually if we want a fresh start
    cursor.execute("DELETE FROM ledger") 
    
    df.to_sql('ledger', conn, if_exists='append', index=False)
    
    conn.commit()
    print(f"✅ Success: Data hardened and moved to Central Vault.")
    conn.close()

if __name__ == "__main__":
    ingest_data()