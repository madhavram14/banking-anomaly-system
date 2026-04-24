import pandas as pd
from database import fetch_transactions
from engine import RiskSentinel
from config import RISK_THRESHOLD

def run_audit():
    print("Initializing Global Sentinel Audit...")
    
    # 1. Fetch data from SQL Vault
    df = fetch_transactions()
    
    if df.empty:
        print("❌ Audit Aborted: No data found in the ledger.")
        return

    # 2. Fix the Timestamp Crash (Day 11 Resilience Patch)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')
    
    # 3. Sort for Temporal Analysis
    df = df.sort_values(by=['city', 'timestamp'])

    sentinel = RiskSentinel(RISK_THRESHOLD)
    
    # 4. Standard Heuristic Evaluation (Row-by-Row)
    df[['risk_score', 'is_suspicious']] = df.apply(
        lambda row: sentinel.evaluate_transaction(row), 
        axis=1, result_type='expand'
    )
    
    # 5. Advanced Velocity Logic (Sliding Window)
    df['time_diff'] = df.groupby('city')['timestamp'].diff().dt.total_seconds()
    
    # FLAG: If transactions in the same city happen within 30 seconds
    velocity_mask = df['time_diff'] < 30
    df.loc[velocity_mask, 'is_suspicious'] = True
    df.loc[velocity_mask, 'risk_score'] += 20  
    
    # 6. Filter for Forensic Results
    df_suspicious = df[df['is_suspicious']].copy()
    
    # 7. Final Column Selection
    columns_to_keep = [
        'txn_id', 'user_tier', 'amount_inr', 'city', 
        'status', 'timestamp', 'risk_score', 'is_suspicious'
    ]
    df_suspicious = df_suspicious[columns_to_keep]
    
    suspicious_count = len(df_suspicious)
    print(f"Audit Complete. Found {suspicious_count} suspicious transactions.")
    
    # 8. Save Forensic Results for Reporter
    df_suspicious.to_csv("audit_results.csv", index=False)

if __name__ == "__main__":
    run_audit()
