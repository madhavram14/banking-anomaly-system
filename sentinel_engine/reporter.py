import os
import pandas as pd
import ollama

def get_llm_reasoning(anomaly_detail):
    """
    Uses local Llama 3 via Ollama for zero-latency, private forensic analysis.
    """
    try:
        response = ollama.chat(model='llama3', messages=[
          {
            'role': 'user',
            'content': f"You are a Senior Banking Fraud Investigator. Provide a 2-sentence forensic summary for this anomaly: {anomaly_detail}",
          },
        ])
        return response['message']['content'].strip()
    except Exception as e:
        return f"Local LLM Error: {str(e)}"

def generate_html_report(alerts_list):
    """
    Generates the professional forensic dashboard.
    """
    df = pd.DataFrame(alerts_list)
    if df.empty:
        print("📭 No alerts to report.")
        return

    count_val = len(df)
    html_template = """
    <html>
    <head>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f1f5f9; padding: 40px; }
            .header { border-bottom: 2px solid #38bdf8; padding-bottom: 10px; margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 12px; overflow: hidden; }
            th { background: #334155; color: #38bdf8; padding: 15px; text-align: left; font-size: 0.85rem; text-transform: uppercase; }
            td { padding: 15px; border-bottom: 1px solid #334155; font-size: 0.9rem; color: #e2e8f0; }
            .ai-insight { color: #38bdf8; font-style: italic; font-weight: 500; }
            .alert-text { color: #f472b6; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📡 Sentinel Forensic Report</h1>
            <p>Detection Engine: <strong>Hybrid (Deterministic + Llama 3)</strong> | Anomalies Found: <strong>REPLACE_COUNT</strong></p>
        </div>
        <table>
            <tr>
                <th>Transaction ID</th>
                <th>Status</th>
                <th>Logic Flags (Triage)</th>
                <th>AI Forensic Insight</th>
            </tr>
    """
    html_template = html_template.replace("REPLACE_COUNT", str(count_val))

    for _, row in df.iterrows():
        html_template += f"""
        <tr>
            <td><code>{row['transaction_id']}</code></td>
            <td class="alert-text">{row['alert']}</td>
            <td>{row['details']}</td>
            <td class="ai-insight">{row.get('ai_analysis', 'No analysis.')}</td>
        </tr>
        """
    html_template += "</table></body></html>"

    with open("audit_report.html", "w") as f:
        f.write(html_template)
    print("🎨 Dashboard Generated: audit_report.html")