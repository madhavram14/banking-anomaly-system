import os
import shutil
from datetime import datetime

def archive_results():
    if os.path.exists("audit_report.html"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        archive_name = f"reports/audit_{timestamp}.html"
        os.makedirs("reports", exist_ok=True)
        shutil.copy("audit_report.html", archive_name)
        print(f"📦 Report archived to: {archive_name}")

if __name__ == "__main__":
    archive_results()