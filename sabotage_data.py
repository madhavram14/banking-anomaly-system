import sqlite3
from datetime import datetime

def inject_faults():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    print("😈 Injecting 'ledger' anomalies using real schema...")

    # 1. Structuring/Smurfing: Rapid small amounts (INR)
    # Adding 'city' to the columns and 'PUNE' to the values
    for i in range(5):
        cursor.execute("""
            INSERT INTO ledger (txn_id, user_tier, amount_inr, city, status, timestamp) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (f'STRUC_{i}', 'Silver', 9000.0, 'PUNE', 'Success', datetime.now().isoformat()))

    # 2. Impossible Large Amount: Finding the "Whale"
    # Also assigning the Whale to PUNE
    cursor.execute("""
        INSERT INTO ledger (txn_id, user_tier, amount_inr, city, status, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, ('WHALE_999', 'Silver', 1000000.0, 'PUNE', 'Success', datetime.now().isoformat()))

    conn.commit()
    conn.close()
    print("✅ Sabotage Complete. The ledger is now dirty with a Pune origin.")

if __name__ == "__main__":
    inject_faults()