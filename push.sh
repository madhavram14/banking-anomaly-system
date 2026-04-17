#!/bin/bash
# Navigate to the project folder
cd "/home/madhav/Documents/Banking Projects/banking-anomaly-system"

# Run the detector to ensure the latest audit_report.html is ready
python3 anomaly_detector.py

# Git commands to update the streak
git add .
git commit -m "Day 5: Automated Heuristic Audit & Multi-Point Detection"
git push origin main
