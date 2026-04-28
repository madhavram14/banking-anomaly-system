# 📡 System Design Specification: Banking Anomaly Sentinel

## 1. Executive Summary
The **Banking Anomaly Sentinel** is a high-performance detection engine designed to identify financial irregularities, including "Structuring" (Smurfing) and high-velocity "Whale" transactions. The system is architected for maximum data integrity, utilizing a hardened SQLite backend and a modular detection pipeline.

## 2. System Architecture
The system follows a **Pipe-and-Filter** architecture, ensuring that data ingestion, risk evaluation, and reporting are decoupled.

### A. Data Layer (The Vault)
* **Engine:** SQLite3
* **Schema:** 10-column hardened ledger.
* **Integrity:** Implements schema reconciliation to prevent data drift during ingestion from disparate sources (CSV/API).

### B. Logic Layer (The Sentinel)
* **Heuristic Engine:** Multi-factor scoring based on `config.py` weights.
* **Key Alarms:**
    * **Structuring (STRUC):** Identifies patterns of transaction breaking intended to bypass regulatory thresholds.
    * **Tier-Adjusted Velocity:** Dynamically adjusts risk thresholds based on User Tiers (Silver, Gold, Platinum).
* **Feature Engineering:** Modularized numerical transformation for future AI/ML model integration (Isolation Forest).

### C. Presentation Layer (The Auditor)
* **Reporter:** Generates a forensic HTML Dashboard.
* **Signal-to-Noise Calibration:** Implements a strict risk-threshold (Default: 40) to filter out "Verified" noise and highlight actionable threats.

## 3. Technical Design Choices

### Why SQLite?
Chosen for its Zero-Configuration footprint and ACID compliance, making the system portable and resilient for local bank-branch auditing before centralizing to a Mainframe.

### Why Feature Engineering?
The project is architected with a "Model-Ready" mindset. By transforming categorical data (Tiers) into numerical ranks, the system is prepared for seamless transition into **Unsupervised Machine Learning**.

### Why Automated Testing?
Utilizes **Pytest** for regression testing. In financial systems, a logic error is a liability; automation ensures that every "Risk Weight" change is verified before deployment.

## 4. Scalability Roadmap
1.  **Phase 1 (Current):** Local Python/SQLite engine with Heuristic rules.
2.  **Phase 2 (Near-term):** Containerization via **Docker** and UI validation via **Playwright**.
3.  **Phase 3 (Target):** Migration to **PostgreSQL** for high-concurrency environments and integration of **Scikit-Learn** for AI-driven anomaly detection.

## 5. Security & Compliance
* **Zero-Trust Logic:** Every transaction is treated as high-risk until the `evaluate_transaction` filter passes it.
* **Audit Trail:** Every calculation is written back to the `ledger` for permanent record-keeping.

---
*Created by Madhav | April 2026*