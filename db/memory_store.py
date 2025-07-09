github_token = None

def set_token(token: str):
    global github_token
    github_token = token



def get_token():
    return github_token

import json
from datetime import datetime
from pathlib import Path

TRACKER_PATH = Path(__file__).parent / "problem_tracker.json"

def read_tracker():
    with open(TRACKER_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_tracker(data: dict):
    with open(TRACKER_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_current_index():
    data = read_tracker()
    return data["current_index"]

def increment_index():
    data = read_tracker()
    data["current_index"] += 1
    write_tracker(data)
    return data["current_index"]


def update_last_commit_date():
    data = read_tracker()
    data["last_commit_date"]=datetime.now().strftime("%Y-%m-%d")
    write_tracker(data)
