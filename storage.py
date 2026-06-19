import json
import os
from dataclasses import asdict

from models import Alarm

DATA_FILE = "alarms.json"


def load_alarms():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return [Alarm(**item) for item in data]


def save_alarms(alarms):
    with open(DATA_FILE, "w") as f:
        json.dump(
            [asdict(alarm) for alarm in alarms],
            f,
            indent=2
        )