
### **Day 11: Sliding Window Analytics**
* **Temporal Velocity Engine:** Refactored `main.py` to calculate `time_diff` between transactions.
* **Smurfing Detection:** Implemented a 30-second sliding window to identify high-frequency bot activity.
* **Dynamic Risk Scoring:** Added a +20 "Velocity Penalty" to transactions that exceed frequency thresholds.
