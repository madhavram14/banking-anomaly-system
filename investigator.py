import sqlite3
import pandas as pd
from langchain_community.llms import Ollama

def get_transaction_details(txn_id):
    conn = sqlite3.connect('bank.db')
    query = f"SELECT * FROM ledger WHERE txn_id = '{txn_id}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df.to_dict('records')

def agent_investigation(txn_id):
    print(f"🕵️ Local Agent starting investigation on {txn_id}...")
    
    details = get_transaction_details(txn_id)
    if not details:
        return "Transaction not found."

    # Use the local model you just downloaded
    llm = Ollama(model="llama3")
    
    prompt = f"""
    You are a Senior Fraud Investigator. Review this transaction ledger entry:
    {details}
    
    Analyze the following:
    1. Is the amount ({details[0]['amount_inr']}) unusual for a {details[0]['user_tier']} user?
    2. Is the time ({details[0]['timestamp']}) a high-risk hour?
    3. Final Verdict: (SANE or ANOMALY)
    """
    
    return llm.invoke(prompt)

if __name__ == "__main__":
    result = agent_investigation("TXN-83237")
    print("\n--- AGENT REASONING ---")
    print(result)