# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bank.db')

RISK_THRESHOLD = 40
WHALE_LIMIT = 500000

# Update these keys to match what engine.py uses
# config.py - Calibration Update
WEIGHTS = {
    "PLACEMENT": 45,      # High amounts
    "STRUCTURING": 40,    # Increase from 30 to 40 to meet the Threshold
    "VELOCITY": 20
}
# Add this to your config.py
CITY_COORDS = {
    "Chennai": (13.0827, 80.2707),
    "Pune": (18.5204, 73.8567),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Delhi": (28.6139, 77.2090)
}