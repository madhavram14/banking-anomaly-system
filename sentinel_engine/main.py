# main.py
from database import fetch_transactions
from engine import RiskSentinel
from config import RISK_THRESHOLD

def run_audit():
    print("Initializing Global Sentinel Audit...")
    df = fetch_transactions()
    sentinel = RiskSentinel(RISK_THRESHOLD)
    
    # 1. Apply the logic
    df[['risk_score', 'is_suspicious']] = df.apply(
        lambda row: sentinel.evaluate_transaction(row), 
        axis=1, result_type='expand'
    )
    
    # 2. Filter for only suspicious hits
    df_suspicious = df[df['is_suspicious']].copy()
    
    # 3. Select the columns we want to keep (including city and status)
    df_suspicious = df_suspicious[[
        'txn_id', 'user_tier', 'amount_inr', 'city', 
        'status', 'timestamp', 'risk_score', 'is_suspicious'
    ]]
    
    suspicious_count = len(df_suspicious)
    print(f"Audit Complete. Found {suspicious_count} suspicious transactions.")
    
    # 4. Save the results
    df_suspicious.to_csv("audit_results.csv", index=False)
if __name__ == "__main__":
    run_audit()