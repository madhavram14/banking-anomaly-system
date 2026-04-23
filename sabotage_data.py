import sqlite3
from datetime import datetime
from config import DB_PATH  # Import the central path

def inject_faults():
    # Connect to the central Source of Truth
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"😈 Injecting anomalies into {DB_PATH}...")

    # 1. Structuring/Smurfing: Rapid small amounts (INR)
    # Adding 'city' column and 'PUNE' value
    for i in range(5):
        cursor.execute("""
            INSERT INTO ledger (txn_id, user_tier, amount_inr, city, status, timestamp) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (f'STRUC_{i}', 'Silver', 9000.0, 'PUNE', 'Success', datetime.now().isoformat()))

    # 2. Impossible Large Amount: Finding the "Whale"
    cursor.execute("""
        INSERT INTO ledger (txn_id, user_tier, amount_inr, city, status, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, ('WHALE_999', 'Silver', 1000000.0, 'PUNE', 'Success', datetime.now().isoformat()))

    conn.commit()
    conn.close()
    print("✅ Sabotage Complete. The ledger is now dirty with a Pune origin.")

if __name__ == "__main__":
    inject_faults()