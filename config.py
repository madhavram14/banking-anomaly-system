import os

# Get the absolute path of the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bank.db')

print(f"📡 System Path Locked: {DB_PATH}")