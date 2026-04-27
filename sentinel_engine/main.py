# sentinel_engine/main.py
import pandas as pd
from database import fetch_transactions
from engine import RiskSentinel
from config import RISK_THRESHOLD
from features import prepare_features
from reporter import generate_html_report

def run_audit():
    print("🚀 Initializing Global Sentinel Audit...")
    
    # 1. Data Ingestion
    df = fetch_transactions()
    if df.empty:
        print("❌ Audit Aborted: No data found in the ledger.")
        return

    # 2. Feature Engineering (Temporal & Numerical)
    df = prepare_features(df)
    
    # 3. Heuristic Evaluation
    sentinel = RiskSentinel(RISK_THRESHOLD)
    df[['risk_score', 'is_suspicious']] = df.apply(
        lambda row: sentinel.evaluate_transaction(row), 
        axis=1, result_type='expand'
    )
    
    # 4. Advanced Velocity & Signal-to-Noise Calibration
    # Velocity Logic (Sliding Window)
    velocity_mask = df['time_diff'] < 30
    df.loc[velocity_mask, 'is_suspicious'] = True
    df.loc[velocity_mask, 'risk_score'] += 20  
    
    # Signal-to-Noise Calibration (Day 12)
    df.loc[df['status'].str.upper() == 'VERIFIED', 'risk_score'] -= 15
    
    # Final Suspicious Flag Update
    df['is_suspicious'] = df['risk_score'] >= RISK_THRESHOLD

    # 5. Reporting
    suspicious_count = df['is_suspicious'].sum()
    print(f"✅ Audit Complete. Found {suspicious_count} suspicious transactions.")
    
    # Save results and trigger HTML report
    df[df['is_suspicious']].to_csv("audit_results.csv", index=False)
    generate_html_report(df)

if __name__ == "__main__":
    run_audit()