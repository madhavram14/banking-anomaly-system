# engine.py
from config import WEIGHTS, WHALE_LIMIT

class RiskSentinel:
    def __init__(self, threshold):
        self.threshold = threshold

    def evaluate_transaction(self, row):
        score = 0
        
        # Placement Check - Updated to 'user_tier' and 'amount_inr'
        if row['user_tier'] == 'Silver' and row['amount_inr'] > WHALE_LIMIT:
            score += WEIGHTS["PLACEMENT"]
            
        # Structuring Check - Matches 'txn_id'
        if str(row['txn_id']).startswith('STRUC'):
            score += WEIGHTS["STRUCTURING"]
            
        return score, score >= self.threshold