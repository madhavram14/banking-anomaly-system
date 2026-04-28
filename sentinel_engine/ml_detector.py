# sentinel_engine/ml_detector.py
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies_ai(df):
    """
    Uses Unsupervised Learning to find patterns the human-written 
    rules might have missed.
    """
    # 1. Select the features we engineered yesterday
    features = ['tier_rank', 'amt_normalized', 'time_diff']
    X = df[features].fillna(0)

    # 2. Initialize the Isolation Forest
    # contamination=0.05 means we expect 5% of transactions to be 'weird'
    model = IsolationForest(contamination=0.05, random_state=42)
    
    # 3. Fit and Predict
    # -1 means Anomaly, 1 means Normal
    df['ai_prediction'] = model.fit_predict(X)
    
    # 4. Convert to a 'Probability' score (0 to 100)
    # This makes it easier for your reporter to display
    scores = model.decision_function(X) 
    df['ai_risk_score'] = (1 - scores) * 50 # Scaling for the dashboard
    
    return df