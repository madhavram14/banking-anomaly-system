import sqlite3
from datetime import datetime
from config import DB_PATH

def inject_sabotage():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. We now provide 10 values per row to match the 'ledger' table
    # Schema: txn_id, user_tier, amount_inr, city, status, timestamp, 
    #         risk_score, is_suspicious, time_diff, location_id (or similar placeholders)
    
    # The last 4 values are 0, False, 0.0, None as placeholders
    struc_data = [
        ('STRUC_001', 'Silver', 5000, 'PUNE', 'SUCCESS', datetime.now().isoformat(), 0, False, 0.0, None),
        ('STRUC_002', 'Silver', 4800, 'PUNE', 'SUCCESS', datetime.now().isoformat(), 0, False, 0.0, None),
        ('STRUC_003', 'Silver', 4900, 'PUNE', 'SUCCESS', datetime.now().isoformat(), 0, False, 0.0, None),
    ]
    
    verified_data = [
        ('TXN_TRUST_99', 'Gold', 900000, 'MUMBAI', 'VERIFIED', datetime.now().isoformat(), 0, False, 0.0, None),
    ]

    # The SQL query now needs 10 question marks
    query = "INSERT INTO ledger VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    try:
        cursor.executemany(query, struc_data)
        cursor.executemany(query, verified_data)
        conn.commit()
        print("💉 Sabotage Injected successfully into the 10-column ledger.")
    except Exception as e:
        print(f"❌ Insertion failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    inject_sabotage()
