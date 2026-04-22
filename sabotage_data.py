import sqlite3
from datetime import datetime

def inject_faults():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("😈 Injecting 'ledger' anomalies using real schema...")

    # 1. Structuring/Smurfing: Rapid small amounts (INR)
    # We'll use a fake txn_id like 'SABOTAGE_001'
    for i in range(5):
        cursor.execute("""
            INSERT INTO ledger (txn_id, user_tier, amount_inr, status, timestamp) 
            VALUES (?, ?, ?, ?, ?)
        """, (f'STRUC_{i}', 'Silver', 9000.0, 'Success', datetime.now().isoformat()))

    # 2. Impossible Large Amount: Finding the "Whale"
    cursor.execute("""
        INSERT INTO ledger (txn_id, user_tier, amount_inr, status, timestamp) 
        VALUES (?, ?, ?, ?, ?)
    """, ('WHALE_999', 'Silver', 1000000.0, 'Success', datetime.now().isoformat()))

    conn.commit()
    conn.close()
    print("✅ Sabotage Complete. The ledger is now dirty.")

if __name__ == "__main__":
    inject_faults()