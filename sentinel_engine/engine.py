# engine.py
from config import WEIGHTS, WHALE_LIMIT

class RiskSentinel:
    def __init__(self, threshold):
        self.threshold = threshold

    def evaluate_transaction(self, row):
        score = 0
        
        # Use .upper() to ensure 'SILVER', 'Silver', and 'silver' all match
        user_tier = str(row['user_tier']).upper()
        
        # Placement Check
        if user_tier == 'SILVER' and row['amount_inr'] > WHALE_LIMIT:
            score += WEIGHTS["PLACEMENT"]
            
        # Structuring Check
        if str(row['txn_id']).startswith('STRUC'):
            score += WEIGHTS["STRUCTURING"]
            
        return score, score >= self.threshold   