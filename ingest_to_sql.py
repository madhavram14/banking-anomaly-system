import sqlite3
import pandas as pd
from config import DB_PATH  # Import the central path

def ingest_data():
    # 1. Connect using the central Source of Truth
    conn = sqlite3.connect(DB_PATH)
    
    # 2. Load the bank-formatted CSV
    df = pd.read_csv('day2_transactions.csv')
    
    # 3. Save it to 'ledger'
    df.to_sql('ledger', conn, if_exists='replace', index=False)
    
    print(f"✅ Success: Data moved to Central SQL Vault: {DB_PATH}")
    conn.close()

if __name__ == "__main__":
    ingest_data()