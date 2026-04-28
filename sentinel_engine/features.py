# sentinel_engine/features.py
import pandas as pd

def prepare_features(df):
    """
    Transforms raw ledger data into engineered features for the Sentinel.
    """
    # 1. Temporal Engineering
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')
    df = df.sort_values(by=['city', 'timestamp'])
    
    # 2. Numerical Mapping (AI-Ready)
    tier_map = {'SILVER': 1, 'GOLD': 2, 'PLATINUM': 3}
    df['tier_rank'] = df['user_tier'].str.upper().map(tier_map).fillna(0)
    
    # 3. Velocity Feature
    # We fillna(0) because the first transaction in a city has no 'previous' time
    df['time_diff'] = df.groupby('city')['timestamp'].diff().dt.total_seconds().fillna(0)
    
    # 4. Normalization (THE MISSING PIECE)
    # AI models perform better when numbers are on a similar scale (e.g., 0 to 100)
    df['amt_normalized'] = df['amount_inr'] / 10000
    
    return df