import json
import pandas as pd
import requests


def fetch_aiid_reports():
    # AIID provides API lookup and dataset export endpoints
    url = "https://incidentdatabase.ai/api/read/incidents"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching AIID data: {e}")
        return []


def load_local_snapshot(file_path):
    # Alternative: Load pre-downloaded JSON export
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    incidents = fetch_aiid_reports()
    print(f"Loaded raw incident records successfully.")