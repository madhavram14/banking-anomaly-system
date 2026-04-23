# 🏛️ Global Sentinel: Banking Anomaly & Risk Engine
**Version:** 2.0 (Day 10 Milestone)  
**Architecture:** Centralized SQL-Vault with Absolute Pathing Logic  

## 📌 Project Overview
Global Sentinel is a high-performance Python and SQL-based auditing system designed to detect illicit financial patterns including Money Laundering (AML), Fee Evasion, and Structuring. This system utilizes a modular "Source of Truth" architecture to handle high-velocity transaction streams and provides forensic reporting on geographic and temporal anomalies.

## 📊 System Architecture

```mermaid
flowchart TD
    A[day2_generator.py: Raw Stream] -->|Ingest| B[(bank.db: SQLite Vault)]
    S[sabotage_data.py: Chaos Monkey] -->|Inject Anomalies| B
    B --> C{Heuristic Risk Engine: main.py}
    C -->|Score < 40| D[Compliant Ledger]
    C -->|Score 40-49| E[Orange Alert: Secondary Review]
    C -->|Score 50+| F[Red Alert: Critical Intervention]
    F --> G[reporter.py: Forensic Analysis Report]