# config.py
DB_PATH = "bank.db"

# Risk Weights
WEIGHTS = {
    "PLACEMENT": 35,  # Large deposits in low tiers
    "LAYERING": 45,   # High-velocity international movement
    "STRUCTURING": 50 # Smurfing patterns
}

# Thresholds
RISK_THRESHOLD = 40
WHALE_LIMIT = 100000