import pandas as pd
import random
from datetime import datetime, timedelta

# 1. BANK POLICY RULES
TIER_FEES = {'Silver': 0.05, 'Gold': 0.02, 'Platinum': 0.00}
FX_RATES = {'USD': 83.50, 'EUR': 91.20, 'MXN': 4.85, 'INR': 1.00}

def generate_bank_data():
    transactions = []
    # Create a small pool of 10 users to ensure repeat activity
    user_pool = [f"USER_{i:03}" for i in range(1, 11)]
    
    for i in range(100):
        user_id = random.choice(user_pool)
        tier = random.choice(['Silver', 'Gold', 'Platinum'])
        curr = random.choice(['USD', 'EUR', 'MXN', 'INR'])
        
        amt_local = random.uniform(10.00, 5000.00)
        rate = FX_RATES[curr]
        amt_inr = round(amt_local * rate, 2)
        fee = round(amt_inr * TIER_FEES[tier], 2) if curr != 'INR' else 0.00
        
        # Incremental timestamps to simulate a day of activity
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 1440))
        
        transactions.append({
            'txn_id': f"TXN-{random.randint(10000, 99999)}",
            'user_id': user_id,
            'user_tier': tier,
            'amount_inr': amt_inr, # Kept as float for SQL compatibility
            'city': random.choice(['PUNE', 'CHENNAI', 'MUMBAI', 'BANGALORE', None]),
            'status': 'SUCCESS',
            'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S")
        })

    # --- ALPHA SABOTAGE: Impossible Travel Scenario ---
    # Manually inject a user appearing in two cities instantly
    target_user = "USER_999"
    base_time = datetime.now()
    
    # Transaction 1: Chennai
    transactions.append({
        'txn_id': "TXN-IMPOSSIBLE-1",
        'user_id': target_user,
        'user_tier': 'Gold',
        'amount_inr': 500.00,
        'city': 'CHENNAI',
        'status': 'SUCCESS',
        'timestamp': base_time.strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # Transaction 2: Pune (Happening only 5 minutes later - Impossible Velocity)
    transactions.append({
        'txn_id': "TXN-IMPOSSIBLE-2",
        'user_id': target_user,
        'user_tier': 'Gold',
        'amount_inr': 750.00,
        'city': 'PUNE',
        'status': 'SUCCESS',
        'timestamp': (base_time + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
    })

    return pd.DataFrame(transactions)

df = generate_bank_data()
df.to_csv("day2_transactions.csv", index=False)
print("✅ Bank Data Factory: 'day2_transactions.csv' generated with 2-decimal precision.")