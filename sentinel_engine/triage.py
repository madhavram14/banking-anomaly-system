from utils import get_velocity, is_impossible_travel

def evaluate_geographical_risk(tx_history):
    """
    Acts as a pre-filter agent. Scans sequential transactions for impossible travel.
    Returns structured data for the LLM investigator.
    """
    flagged_anomalies = []
    
    # Iterate through transactions to compare city jumps
    for i in range(1, len(tx_history)):
        prev_tx = tx_history[i-1]
        curr_tx = tx_history[i]
        
        # Calculate time difference
        time_diff = curr_tx['timestamp_hours'] - prev_tx['timestamp_hours']
        
        # Calculate speed using your Haversine utility
        velocity = get_velocity(prev_tx['city'], curr_tx['city'], time_diff)
        
        if is_impossible_travel(velocity):
            flagged_anomalies.append({
                "transaction_id": curr_tx['id'],
                "alert": "IMPOSSIBLE_TRAVEL",
                "details": f"Velocity of {velocity:.2f} km/h detected between {prev_tx['city']} and {curr_tx['city']}.",
                "recommendation": "LLM_DEEP_DIVE_REQUIRED"
            })
            
    return flagged_anomalies

# Quick local test
if __name__ == "__main__":
    # Mock data: A transaction in Pune at hour 10, then Chennai at hour 11. (1 hour gap)
    mock_history = [
        {"id": "TXN_001", "city": "PUNE", "timestamp_hours": 10},
        {"id": "TXN_002", "city": "CHENNAI", "timestamp_hours": 11}
    ]
    
    findings = evaluate_geographical_risk(mock_history)
    print(f"Agent Triage Complete. Anomalies found: {len(findings)}")
    for f in findings:
        print(f)