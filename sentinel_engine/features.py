# sentinel_engine/features.py
import pandas as pd

def prepare_features(df):
    """
    Transforms raw ledger data into engineered features for the Sentinel.
    """
    # 1. Temporal Engineering (Day 11 Resilience Patch)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')
    df = df.sort_values(by=['city', 'timestamp'])
    
    # 2. Numerical Mapping (AI-Ready)
    tier_map = {'SILVER': 1, 'GOLD': 2, 'PLATINUM': 3}
    df['tier_rank'] = df['user_tier'].str.upper().map(tier_map).fillna(0)
    
    # 3. Velocity Feature: Time difference between transactions in the same city
    df['time_diff'] = df.groupby('city')['timestamp'].diff().dt.total_seconds()
    
    return df