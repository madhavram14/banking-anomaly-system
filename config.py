import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bank.db')

RISK_THRESHOLD = 40
WHALE_LIMIT = 500000

WEIGHTS = {
    "PLACEMENT": 45,
    "STRUCTURING": 40,
    "VELOCITY": 20
}

print(f"📡 System Configuration Loaded | DB: {DB_PATH}")
