
import pandas as pd
from datetime import datetime
from sentinel_engine.database import fetch_transactions
import sentinel_engine.utils as utils  # For the Haversine velocity math

def run_audit():
    # 1. Pull the Identity-Sorted Data from the SQL Vault
    # This ensures transactions are grouped by user and ordered by time
    df = fetch_transactions()
    
    if df.empty:
        print("❌ Error: No data found in the ledger.")
        return

    # 2. Initialize Spatiotemporal Memory
    user_state = {}  # Format: { 'USER_ID': (last_city, last_timestamp) }
    velocities = []
    is_impossible = []

    # 3. The Sequential Detection Loop
    # We move from 'Isolated Rows' to 'User Journeys'
    for index, row in df.iterrows():
        u_id = row['user_id']
        # Clean city data for the coordinate map
        c_city = str(row['city']).upper() if row['city'] and str(row['city']) != 'nan' else "UNKNOWN"
        c_time = datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S")
        
        velocity = 0
        impossible_flag = False
        
        # Check if we have seen this user previously in the sorted sequence
        if u_id in user_state:
            prev_city, prev_time = user_state[u_id]
            
            # Calculate hours elapsed between transactions
            time_diff = (c_time - prev_time).total_seconds() / 3600
            
            # Use Haversine utility to get velocity (km/h)
            velocity = utils.get_velocity(prev_city, c_city, time_diff)

            # Commercial Jet Threshold: 900 km/h
            if velocity > 900:
                impossible_flag = True
        
        # Update memory: Current state becomes the 'previous' state for the next txn
        user_state[u_id] = (c_city, c_time)
        
        velocities.append(round(velocity, 2))
        is_impossible.append(impossible_flag)

    # Attach new intelligence columns to the DataFrame
    df['velocity_kmh'] = velocities
    df['impossible_travel'] = is_impossible

    # 4. Updated Risk Scoring (Prioritizing Spatiotemporal Breaches)
    def calculate_risk_score(row):
        score = 0
        
        # PRIMARY RULE: Physical Impossibility
        if row['impossible_travel']:
            score += 100 
            
        # SECONDARY RULE: Placement Risk (Silver Tier high volume)
        if row['user_tier'] == 'Silver' and float(row['amount_inr']) > 100000:
            score += 35
            
        # TERTIARY RULE: Massive Volume
        if float(row['amount_inr']) > 900000:
            score += 50
            
        return score

    df['risk_score'] = df.apply(calculate_risk_score, axis=1)

    # 5. Dashboard Styling Logic
    def apply_color(row):
        if row['impossible_travel']:
            # Violent Purple for Physical Breach
            return ['background-color: #8e44ad; color: white; font-weight: bold'] * len(row)
        elif row['risk_score'] >= 50:
            # Critical Financial Risk
            return ['background-color: #c0392b; color: white; font-weight: bold'] * len(row)
        elif row['risk_score'] >= 35:
            # Moderate Risk
            return ['background-color: #f39c12; color: white'] * len(row)
        return [''] * len(row)

    styled_df = df.style.apply(apply_color, axis=1)

    # 6. Build the Global Sentinel HTML Report
    html_header = """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Global Sentinel - Pune Phase Audit</title>
        <style>
            body { font-family: 'Inter', sans-serif; margin: 40px; background-color: #f0f2f5; }
            h1 { color: #1a2a6c; border-bottom: 3px solid #1a2a6c; padding-bottom: 10px; }
            .summary-box { 
                padding: 20px; margin-bottom: 30px; border-radius: 8px; 
                border-left: 10px solid #8e44ad; background-color: #fff;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            table { border-collapse: collapse; width: 100%; background: white; font-size: 0.9em; }
            th { background-color: #1a2a6c; color: white; padding: 12px; text-align: left; }
            td { padding: 10px; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <h1>🏛️ Global Sentinel: Spatiotemporal Audit</h1>
        <div class="summary-box">
            <strong>SYSTEM STATUS: PUNE WORKSPACE ACTIVE</strong><br>
            Tracking <b>Velocity Impossibilities</b> and High-Volume Layering. 
            Purple highlights indicate physical location breaches.
        </div>
    """
    
    html_footer = f"""
        <p style="margin-top: 20px; color: #7f8c8d; font-size: 0.8em;">
            Spatiotemporal Engine v2.1 | Pune Phase | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </p>
    </body>
    </html>
    """

    with open('audit_report.html', 'w') as f:
        f.write(html_header + styled_df.to_html() + html_footer)
    
    print("\n" + "="*45)
    print("🚀 PUNE PHASE: Spatiotemporal Audit Complete!")
    print(f"📡 Report Generated: audit_report.html")
    print("="*45)

if __name__ == "__main__":
    run_audit()