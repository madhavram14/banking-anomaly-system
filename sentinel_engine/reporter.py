# sentinel_engine/reporter.py
import os

def generate_html_report(df):
    """
    Generates a professional forensic dashboard with AI-verified badges.
    """
    # 1. Filter for the suspicious hits
    suspicious_df = df[df['is_suspicious'] == True].copy()
    count_val = len(suspicious_df)
    
    # 2. Define the HTML and CSS Template
    # We use a placeholder "REPLACE_COUNT" to avoid .format() conflicts with CSS braces
    html_template = """
    <html>
    <head>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f1f5f9; padding: 40px; }
            .header { border-bottom: 2px solid #38bdf8; padding-bottom: 10px; margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 12px; overflow: hidden; }
            th { background: #334155; color: #38bdf8; padding: 15px; text-align: left; font-size: 0.85rem; text-transform: uppercase; }
            td { padding: 15px; border-bottom: 1px solid #334155; font-size: 0.9rem; color: #e2e8f0; }
            .critical-row { background: rgba(139, 92, 246, 0.1); border-left: 5px solid #8b5cf6; }
            .ai-badge { background: #8b5cf6; color: white; padding: 4px 10px; border-radius: 20px; font-size: 0.65rem; font-weight: bold; }
            .score-highlight { color: #38bdf8; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📡 Sentinel Forensic Report</h1>
            <p>Detection Engine: <strong>Hybrid (Heuristics + Isolation Forest)</strong> | Anomalies: <strong>REPLACE_COUNT</strong></p>
        </div>
        <table>
            <tr>
                <th>Status</th>
                <th>Transaction ID</th>
                <th>User Tier</th>
                <th>Amount (INR)</th>
                <th>City</th>
                <th>Rule Score</th>
                <th>AI Risk Score</th>
            </tr>
    """
    
    # Insert the count safely
    html_template = html_template.replace("REPLACE_COUNT", str(count_val))

    # 3. Build the Data Rows
    for _, row in suspicious_df.iterrows():
        # Check for AI confirmation
        is_ai = row.get('is_ai_verified', False)
        row_class = "critical-row" if is_ai else ""
        ai_badge = '<span class="ai-badge">AI VERIFIED</span>' if is_ai else ""
        
        # Format values for professional display
        ai_score = f"{row.get('ai_risk_score', 0):.1f}%"
        formatted_amt = f"₹{row['amount_inr']:,.2f}"
        
        html_template += f"""
        <tr class="{row_class}">
            <td>{ai_badge}</td>
            <td>{row['txn_id']}</td>
            <td>{row['user_tier']}</td>
            <td>{formatted_amt}</td>
            <td>{row['city']}</td>
            <td>{row['risk_score']}</td>
            <td class="score-highlight">{ai_score}</td>
        </tr>
        """

    # 4. Close the tags
    html_template += """
        </table>
    </body>
    </html>
    """
    
    # 5. Write to file
    with open("audit_report.html", "w") as f:
        f.write(html_template)
    
    print("🎨 Professional Dashboard Generated: audit_report.html")