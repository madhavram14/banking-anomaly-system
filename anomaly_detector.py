import sqlite3
import pandas as pd

def run_audit():
    # 1. Connect to the SQL Vault
    conn = sqlite3.connect('bank.db')
    
    # 2. Pull all data to analyze
    query = "SELECT * FROM ledger"
    df = pd.read_sql_query(query, conn)
    
    # 3. The "Financial Duty" Risk Engine
    def calculate_risk_score(row):
        score = 0
        # Rule 1: Placement Risk (Silver moving large INR)
        if row['user_tier'] == 'Silver' and row['amount_inr'] > 100000:
            score += 35
        # Rule 2: Layering Risk (International + 0 Fees)
        if row['currency'] != 'INR' and row['fee_charged'] == 0:
            score += 45
        # Rule 3: Structuring / Smurfing Fingerprint
        if 'STRUC' in str(row['txn_id']) or row['amount_inr'] > 900000:
            score += 50
        return score

    # Apply the Score
    df['risk_score'] = df.apply(calculate_risk_score, axis=1)

    # Flag suspicious if score hits the threshold
    df['is_suspicious'] = df['risk_score'] >= 40

    # 4. Create the "Heatmap" Styling
    def apply_color(row):
        if row['risk_score'] >= 50:
            # Critical Risk: Bold Red
            return ['background-color: #ff4d4d; color: white; font-weight: bold'] * len(row)
        elif row['risk_score'] >= 35:
            # Moderate Risk: Alert Orange
            return ['background-color: #ffe6cc; color: #cc5200'] * len(row)
        return [''] * len(row)

    # Apply the styles
    styled_df = df.style.apply(apply_color, axis=1)

    # 5. Build the Full HTML Page
    html_header = """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Global Sentinel - Audit Report</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f4f7f6; }
            h1 { color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
            .summary-box { 
                padding: 20px; 
                margin-bottom: 30px; 
                border-radius: 8px; 
                border-left: 10px solid #e74c3c;
                background-color: #fff;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            table { border-collapse: collapse; width: 100%; background: white; }
            th { background-color: #2c3e50; color: white; padding: 12px; text-align: left; }
            td { padding: 10px; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <h1>🏛️ Banking Anomaly Audit Report</h1>
        <div class="summary-box">
            <strong>SYSTEM STATUS: ATTENTION REQUIRED</strong><br>
            Multi-point Risk Scoring activated. Rows are highlighted based on <b>Placement, Layering, and Structuring</b> fingerprints.
        </div>
    """
    
    html_footer = f"""
        <p style="margin-top: 20px; color: #7f8c8d; font-size: 0.8em;">
            Report generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
        </p>
    </body>
    </html>
    """

    final_html = html_header + styled_df.to_html() + html_footer

    with open('audit_report.html', 'w') as f:
        f.write(final_html)
    
    print("\n" + "="*40)
    print("🎨 SUCCESS: Heatmapped Risk Report Generated!")
    print("="*40)
    conn.close()

if __name__ == "__main__":
    run_audit()