import pandas as pd
import os
from datetime import datetime
import shutil

def generate_report():
    if not os.path.exists("audit_results.csv"):
        print("❌ Error: Run main.py first.")
        return

    df = pd.read_csv("audit_results.csv")
    total_anomalies = len(df)
    
    # --- DAY 13: REGIONAL ANALYSIS ---
    pune_df = df[df['city'].str.upper() == 'PUNE']
    pune_count = len(pune_df)
    pune_percentage = (pune_count / total_anomalies * 100) if total_anomalies > 0 else 0

    # Professional CSS with "High Risk" styling
    html_content = f"""
    <html>
    <head>
        <title>Sentinel Forensic Audit</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f8fafc; }}
            h2 {{ color: #1e293b; margin-bottom: 5px; }}
            .summary-container {{ display: flex; gap: 20px; margin-bottom: 20px; }}
            .card {{ background: #fff; padding: 15px; border-radius: 8px; border-left: 5px solid #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex: 1; }}
            .pune-card {{ border-left-color: #e11d48; }}
            table {{ width: 100%; border-collapse: collapse; background: white; }}
            th {{ background-color: #334155; color: white; padding: 12px; text-align: left; position: sticky; top: 0; }}
            td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; }}
            tr {{ background-color: #fee2e2; color: #991b1b; font-weight: 500; }}
            tr:hover {{ background-color: #fecaca; }}
        </style>
    </head>
    <body>
        <h2>🏛️ Global Sentinel: Anomaly Forensic Report</h2>
        <p style="color: #64748b; margin-bottom: 20px;">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="summary-container">
            <div class="card">
                <b>Total Flags Detected</b><br>
                <span style="font-size: 24px;">{total_anomalies}</span>
            </div>
            <div class="card pune-card">
                <b>📍 Pune Hotspot Concentration</b><br>
                <span style="font-size: 24px;">{pune_percentage:.1f}%</span> ({pune_count} hits)
            </div>
        </div>

        <table>
            <thead>
                <tr>{''.join(f'<th>{col.replace("_", " ").title()}</th>' for col in df.columns)}</tr>
            </thead>
            <tbody>
                {''.join(f'<tr>{"".join(f"<td>{val}</td>" for val in row)}</tr>' for row in df.values)}
            </tbody>
        </table>
    </body>
    </html>
    """

    with open("audit_report.html", "w") as f:
        f.write(html_content)
    
    # --- DAY 13: AUTOMATED ARCHIVING ---
    os.makedirs("reports", exist_ok=True)
    archive_path = f"reports/audit_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    shutil.copy("audit_report.html", archive_path)
    
    print(f"✅ Success: Rendered {total_anomalies} rows.")
    print(f"📦 Archive Created: {archive_path}")

if __name__ == "__main__":
    generate_report()