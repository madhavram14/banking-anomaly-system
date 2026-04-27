# sentinel_engine/reporter.py
import os

def generate_html_report(df):
    suspicious_df = df[df['is_suspicious'] == True].copy()
    
    # Simple formatting for the report
    html_table = suspicious_df[['txn_id', 'user_tier', 'amount_inr', 'city', 'risk_score']].to_html(
        classes='high-risk', index=False, border=0
    )

    html_template = f"""
    <html>
    <head>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: white; padding: 40px; }}
            .high-risk {{ width: 100%; border-collapse: collapse; }}
            th {{ background: #333; padding: 10px; }}
            td {{ padding: 10px; border-bottom: 1px solid #444; background: rgba(255, 0, 0, 0.1); }}
            .header {{ border-bottom: 2px solid red; padding-bottom: 10px; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📡 Sentinel Forensic Report</h1>
            <p>Anomalies Detected: {len(suspicious_df)}</p>
        </div>
        {html_table}
    </body>
    </html>
    """
    
    with open("audit_report.html", "w") as f:
        f.write(html_template)
    print("🎨 HTML Report generated: audit_report.html")