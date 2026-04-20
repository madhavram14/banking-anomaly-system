# main.py
from database import fetch_transactions
from engine import RiskSentinel
from config import RISK_THRESHOLD

def run_audit():
    print("Initializing Global Sentinel Audit...")
    df = fetch_transactions()
    sentinel = RiskSentinel(RISK_THRESHOLD)
    
    # Apply the logic
    df[['risk_score', 'is_suspicious']] = df.apply(
        lambda row: sentinel.evaluate_transaction(row), 
        axis=1, result_type='expand'
    )
    
    suspicious_count = df['is_suspicious'].sum()
    print(f"Audit Complete. Found {suspicious_count} suspicious transactions.")
    
    # Save the results
    df[df['is_suspicious']].to_csv("audit_results.csv", index=False)

if __name__ == "__main__":
    run_audit()