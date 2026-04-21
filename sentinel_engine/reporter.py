import pandas as pd

def analyze_anomalies():
    df = pd.read_csv("audit_results.csv")
    
    print("\n--- 🔍 GEOGRAPHIC CLUSTER ANALYSIS ---")
    # This fills the empty gaps with 'UNKNOWN' so they show up
    df['city'] = df['city'].fillna('UNKNOWN')
    city_counts = df['city'].value_counts()
    print(city_counts)
    
    print("\n--- ⏱️ TEMPORAL BURST ANALYSIS ---")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    time_span = df['timestamp'].max() - df['timestamp'].min()
    print(f"Total span: {time_span.total_seconds():.4f} seconds")
    
    if time_span.total_seconds() < 0.01:
        print("CRITICAL: Millisecond-level bot activity detected!")

if __name__ == "__main__":
    analyze_anomalies()