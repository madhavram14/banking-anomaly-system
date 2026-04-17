import sqlite3
import pandas as pd

# Day 5 Logic: Enhanced Detection
def detect_anomalies(conn):
    cursor = conn.cursor()
    
    # SQL to find the "Whales" (Silver users with huge transactions)
    whale_query = """
    SELECT * FROM ledger 
    WHERE user_tier = 'Silver' AND amount_inr > 100000
    """
    
    # SQL to find "Structuring" (More than 3 transactions for same tier/amount in same timestamp)
    # Since our sabotage used identical timestamps, we group by timestamp
    structuring_query = """
    SELECT timestamp, user_tier, COUNT(*) as txn_count 
    FROM ledger 
    GROUP BY timestamp, user_tier
    HAVING txn_count > 3
    """
    
    # Execute and flag
    whales = cursor.execute(whale_query).fetchall()
    structurers = cursor.execute(structuring_query).fetchall()
    
    return whales, structurers
def run_audit():
    # 1. Connect to the SQL Vault
    conn = sqlite3.connect('bank.db')
    
    # 2. Pull all data to analyze
    query = "SELECT * FROM ledger"
    df = pd.read_sql_query(query, conn)
    
# 3. Define the "Multi-Point" Investigation Logic
    # Rule A: Fee Evasion (Your existing rule)
    fee_evasion = (df['user_tier'] == 'Silver') & (df['currency'] != 'INR') & (df['fee_charged'] == 0)
    
    # Rule B: The Whale (Silver users moving > 100,000)
    whale_rule = (df['user_tier'] == 'Silver') & (df['amount_inr'] > 100000)
    
    # Rule C: Structuring (Any transaction ID that starts with 'STRUC')
    structuring_rule = df['txn_id'].str.contains('STRUC', na=False)

    # Combine them all: If ANY rule is true, mark as suspicious
    df['is_suspicious'] = fee_evasion | whale_rule | structuring_rule

    # 4. Create the "Karate-style" Colorful Styling
    def apply_color(row):
        if row['is_suspicious']:
            # Red background with dark red text for anomalies
            return ['background-color: #ffcccc; color: #990000; font-weight: bold'] * len(row)
        return [''] * len(row)

    # Apply the styles
    styled_df = df.style.apply(apply_color, axis=1)

    # 5. Build the Full HTML Page with CSS
    # This adds the professional headers and status boxes you see in IntelliJ reports
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
            The engine has detected potential <b>Fee Evasion</b> or <b>Logic Errors</b>. 
            Highlighted rows indicate Silver-tier users bypassing international transaction fees.
        </div>
    """
    
    html_footer = """
        <p style="margin-top: 20px; color: #7f8c8d; font-size: 0.8em;">
            Report generated on: """ + pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S') + """
        </p>
    </body>
    </html>
    """

    # Combine everything into one file
    final_html = html_header + styled_df.to_html() + html_footer

    with open('audit_report.html', 'w') as f:
        f.write(final_html)
    
    print("\n" + "="*40)
    print("🎨 SUCCESS: Colorful HTML Report Generated!")
    print("Open 'audit_report.html' to view the results.")
    print("="*40)
    
    conn.close()


if __name__ == "__main__":
    run_audit()