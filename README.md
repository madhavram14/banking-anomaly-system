# 🏛️ Global Sentinel: Banking Anomaly & Risk Engine

A high-performance Python and SQL-based auditing system designed to detect illicit financial patterns including Money Laundering (AML), Fee Evasion, and Structuring. This system is built for scalability, utilizing optimized database indexing and modular architecture to handle high-velocity transaction streams.

## 📊 System Architecture

```mermaid
flowchart TD
    A[Raw Transaction Stream] --> B[(SQLite Vault)]
    B --> C{Heuristic Risk Engine}
    C -->|Score < 40| D[Compliant Ledger]
    C -->|Score 40-49| E[Orange Alert: Secondary Review]
    C -->|Score 50+| F[Red Alert: Critical Intervention]
    F --> G[Forensic Analysis Report]