from config import WEIGHTS, WHALE_LIMIT
from utils import get_velocity, is_impossible_travel
from reporter import get_llm_reasoning, generate_html_report

class RiskSentinel:
    def __init__(self, threshold):
        self.threshold = threshold

    def evaluate_transaction(self, row, prev_row=None):
        score = 0
        reasons = []
        
        # 1. Existing AML Logic (Placement & Structuring)
        user_tier = str(row['user_tier']).upper()
        if user_tier == 'SILVER' and row['amount_inr'] > WHALE_LIMIT:
            score += WEIGHTS["PLACEMENT"]
            reasons.append("High-value Placement check triggered.")
            
        if str(row['txn_id']).startswith('STRUC'):
            score += WEIGHTS["STRUCTURING"]
            reasons.append("Structuring pattern detected in ID.")

        # 2. New Geographical Vector (Impossible Travel)
        if prev_row:
            time_diff = row['timestamp_hours'] - prev_row['timestamp_hours']
            velocity = get_velocity(prev_row['city'], row['city'], time_diff)
            
            if is_impossible_travel(velocity):
                score += 50  # Assign a high weight to geo-anomalies
                reasons.append(f"Impossible Travel: {velocity:.2f} km/h detected.")

        return score, score >= self.threshold, "; ".join(reasons)

def run_batch_investigation(batch_data):
    sentinel = RiskSentinel(threshold=40)
    final_alerts = []

    print("--- 🛡️ Sentinel Engine: Multi-Vector Scan ---")

    for i in range(len(batch_data)):
        curr_tx = batch_data[i]
        prev_tx = batch_data[i-1] if i > 0 else None
        
        score, flagged, detail_text = sentinel.evaluate_transaction(curr_tx, prev_tx)

        if flagged:
            print(f"[*] Flagged Transaction {curr_tx['txn_id']}. Analyzing with Llama 3...")
            # Hand off to the LLM for forensic reasoning
            ai_insight = get_llm_reasoning(detail_text)
            
            final_alerts.append({
                "transaction_id": curr_tx['txn_id'],
                "alert": "HIGH_RISK_ANOMALY",
                "details": detail_text,
                "ai_analysis": ai_insight
            })

    # Generate the unified HTML Dashboard
    generate_html_report(final_alerts)
    print("--- ✅ Scan Complete. Dashboard Updated. ---")

if __name__ == "__main__":
    # Mock Batch including your Pune/Chennai flow
    mock_batch = [
        {"txn_id": "TXN_001", "user_tier": "Gold", "amount_inr": 5000, "city": "PUNE", "timestamp_hours": 10},
        {"txn_id": "STRUC_99", "user_tier": "Silver", "amount_inr": 150000, "city": "CHENNAI", "timestamp_hours": 11}, # Structuring + Velocity
    ]
    run_batch_investigation(mock_batch)