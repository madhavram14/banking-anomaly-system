# sentinel_engine/reporter.py
import pandas as pd
import os

# Inside sentinel_engine/reporter.py

def generate_report():
    df = pd.read_csv("audit_results.csv")
    total_anomalies = len(df)

    # Professional CSS with "High Risk" styling
    html_content = f"""
    <html>
    <head>
        <title>Sentinel Forensic Audit</title>
        <style>
            body {{ font-family: sans-serif; margin: 20px; background-color: #f8fafc; }}
            h2 {{ color: #1e293b; }}
            .summary {{ background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: inline-block; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }}
            th {{ background-color: #334155; color: white; padding: 12px; text-align: left; position: sticky; top: 0; }}
            td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; }}
            
            /* THIS IS THE KEY: Every row in audit_results.csv IS suspicious, so highlight them all */
            tr {{ background-color: #fee2e2; color: #991b1b; font-weight: 500; }}
            tr:hover {{ background-color: #fecaca; }}
        </style>
    </head>
    <body>
        <h2>🏛️ Global Sentinel: Anomaly Forensic Report</h2>
        <div class="summary">
            <b>Total Flags Detected:</b> {total_anomalies} <br>
            <b>Report Status:</b> 🔴 ATTENTION REQUIRED
        </div>
        <table>
            <tr>
                {''.join(f'<th>{col}</th>' for col in df.columns)}
            </tr>
            {''.join(f'<tr>{"".join(f"<td>{val}</td>" for val in row)}</tr>' for row in df.values)}
        </table>
    </body>
    </html>
    """

    with open("audit_report.html", "w") as f:
        f.write(html_content)
    
    print(f"✅ Success: Rendered {total_anomalies} highlighted rows.")
if __name__ == "__main__":
    generate_report()