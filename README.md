

# 🏛️ Global Sentinel: Banking Anomaly & Risk Engine

A high-performance Python and SQL-based auditing system designed to detect illicit financial patterns including Money Laundering (AML), Fee Evasion, and Structuring.

## 📊 System Architecture

```mermaid
flowchart TD
    A[Raw Transaction Stream] --> B[(SQLite Vault)]
    B --> C{Heuristic Risk Engine}
    C -->|Score < 40| D[Compliant Ledger]
    C -->|Score 40-49| E[Orange Alert: Secondary Review]
    C -->|Score 50+| F[Red Alert: Critical Intervention]
    F --> G[HTML Heatmap Report]
    
## 🚀 Optimization & Scalability
- **Indexing:** Implemented B-Tree composite indexes on `(user_id, timestamp)` to reduce query complexity from O(n²) to O(n log n).
- **Modular Architecture:** Refactored the engine into a decoupled OOP structure (Config, Database, Engine, Main) for production-grade maintainability.
- **Forensic Logic:** Successfully identified "Structuring" patterns (sub-threshold smurfing) using millisecond-precision timestamp analysis.