# 🏛️ Global Sentinel: Anomaly Detection System

A high-performance forensic audit engine designed to identify banking anomalies, structured layering (smurfing), and velocity-based fraud patterns in SQL ledgers.

## 🚀 Key Features
* **Temporal Burst Analysis:** Detects rapid-fire transactions within a 30-second window.
* **Whale Detection:** Identifies high-value transfers relative to user tier.
* **Signal-to-Noise Calibration:** Automated exclusion of 'Verified Merchants' to reduce false positives.
* **Geographic Hotspotting:** Real-time clustering of suspicious activity by city (Current Target: Pune).

## 🛠️ Technical Stack
* **Engine:** Python 3.12 (Pandas, NumPy)
* **Database:** SQLite3 (Hardened Schema)
* **Verification:** PyTest-style Unit Testing
* **UI:** HTML5/CSS3 Forensic Dashboard