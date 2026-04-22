import pandas as pd
import random
from datetime import datetime

# 1. BANK POLICY RULES
TIER_FEES = {'Silver': 0.05, 'Gold': 0.02, 'Platinum': 0.00}
FX_RATES = {'USD': 83.50, 'EUR': 91.20, 'MXN': 4.85, 'INR': 1.00}

def generate_bank_data():
    transactions = []
    for i in range(100):
        tier = random.choice(['Silver', 'Gold', 'Platinum'])
        curr = random.choice(['USD', 'EUR', 'MXN', 'INR'])
        
        # Generating a realistic local amount
        amt_local = random.uniform(10.00, 5000.00)
        
        # 2. BANKING MATH (Ensuring 2 decimal precision)
        rate = FX_RATES[curr]
        amt_inr = round(amt_local * rate, 2)
        
        # Fee applies to International transfers based on Tier
        fee = round(amt_inr * TIER_FEES[tier], 2) if curr != 'INR' else 0.00
        
        transactions.append({
            'txn_id': f"TXN-{random.randint(10000, 99999)}", # Bank-style ID
            'user_tier': tier,
            'currency': curr,
            'amount_local': f"{amt_local:.2f}",
            'fx_rate': f"{rate:.2f}",
            'amount_inr': f"{amt_inr:.2f}",
            'fee_charged': f"{fee:.2f}",
            'city': random.choice(['PUNE', 'CHENNAI', 'KOCHI', 'THRISSUR', None]), # Added None to test the UNKNOWN failsafe'city': random.choice(['PUNE', 'CHENNAI', 'KOCHI', 'THRISSUR', None]), # Added None to test the UNKNOWN failsafe
            'status': 'SUCCESS',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return pd.DataFrame(transactions)

df = generate_bank_data()
df.to_csv("day2_transactions.csv", index=False)
print("✅ Bank Data Factory: 'day2_transactions.csv' generated with 2-decimal precision.")