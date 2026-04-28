# sentinel_engine/main.py
import pandas as pd
from database import fetch_transactions
from engine import RiskSentinel
from config import RISK_THRESHOLD
from features import prepare_features
from reporter import generate_html_report
from ml_detector import detect_anomalies_ai  # NEW: AI Logic

def run_audit():
    print("🚀 Initializing Global Sentinel Audit (Hybrid Mode)...")
    
    # 1. Data Ingestion
    df = fetch_transactions()
    if df.empty:
        print("❌ Audit Aborted: No data found in the ledger.")
        return

    # 2. Feature Engineering (Temporal & Numerical)
    # This prepares the numerical columns the AI needs to "see"
    df = prepare_features(df)
    
    # 3. AI Intelligence Layer (Unsupervised ML)
    # This identifies outliers based on data patterns, not just rules
    print("🤖 Running Isolation Forest analysis...")
    df = detect_anomalies_ai(df)
    
    # 4. Heuristic Evaluation (Human-written Rules)
    sentinel = RiskSentinel(RISK_THRESHOLD)
    df[['risk_score', 'is_suspicious']] = df.apply(
        lambda row: sentinel.evaluate_transaction(row), 
        axis=1, result_type='expand'
    )
    
    # 5. Advanced Velocity & Signal-to-Noise Calibration
    # Velocity Logic (Sliding Window)
    velocity_mask = df['time_diff'] < 30
    df.loc[velocity_mask, 'is_suspicious'] = True
    df.loc[velocity_mask, 'risk_score'] += 20  
    
    # Signal-to-Noise Calibration (Day 12)
    df.loc[df['status'].str.upper() == 'VERIFIED', 'risk_score'] -= 15
    
    # 6. Hybrid Convergence Logic
    # Update suspicion based on the final calibrated score
    df['is_suspicious'] = df['risk_score'] >= RISK_THRESHOLD

    # FLAG: "Critical" anomalies where Human Rules AND AI agree
    # This is a high-confidence signal (AI pred -1 means anomaly)
    df['is_ai_verified'] = (df['is_suspicious']) & (df['ai_prediction'] == -1)

    # 7. Reporting & Output
    suspicious_count = df['is_suspicious'].sum()
    ai_verified_count = df['is_ai_verified'].sum()
    
    print(f"✅ Audit Complete.")
    print(f"   - Total Flags: {suspicious_count}")
    print(f"   - AI-Verified Criticals: {ai_verified_count}")
    
    # Save results (including new AI columns)
    df[df['is_suspicious']].to_csv("audit_results.csv", index=False)
    
    # Trigger the enhanced HTML report
    generate_html_report(df)

if __name__ == "__main__":
    run_audit()