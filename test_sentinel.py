# test_sentinel.py
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sentinel_engine.engine import RiskSentinel

def test_engine():
    sentinel = RiskSentinel(threshold=40)
    
    print("🧪 Starting Forensic Unit Tests...")

    # Test 1: High Amount (Whale) - Adding dummy txn_id and city
    whale_txn = {
        'txn_id': 'TXN_999', 
        'amount_inr': 600000, 
        'user_tier': 'SILVER',
        'city': 'CHENNAI'
    }
    score, flagged = sentinel.evaluate_transaction(whale_txn)
    print(f"Test 1 (Whale): Score {score}, Flagged: {flagged}")
    assert flagged == True, "❌ Error: Whale was not flagged!"

    # Test 2: Low Amount (Safe)
    safe_txn = {
        'txn_id': 'TXN_001', 
        'amount_inr': 1500, 
        'user_tier': 'PLATINUM',
        'city': 'MUMBAI'
    }
    score, flagged = sentinel.evaluate_transaction(safe_txn)
    print(f"Test 2 (Safe):  Score {score}, Flagged: {flagged}")
    assert flagged == False, "❌ Error: Safe transaction was flagged!"

    # Test 3: Structured Transaction (Specific ID Marker)
    struc_txn = {
        'txn_id': 'STRUC_123', 
        'amount_inr': 5000, 
        'user_tier': 'GOLD',
        'city': 'PUNE'
    }
    score, flagged = sentinel.evaluate_transaction(struc_txn)
    print(f"Test 3 (Struc): Score {score}, Flagged: {flagged}")
    assert flagged == True, "❌ Error: Structured ID was not flagged!"

    print("\n✅ SUCCESS: Risk Engine logic fully verified.")

if __name__ == "__main__":
    test_engine()