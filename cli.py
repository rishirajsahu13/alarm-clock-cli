from uuid import uuid4

from models import Alarm
from storage import load_alarms, save_alarms


def add_alarm(trigger_time, label, repeat_daily):
    alarms = load_alarms()

    alarms.append(
        Alarm(
            id=str(uuid4())[:8],
            trigger_time=trigger_time,
            label=label,
            repeat_daily=repeat_daily,
        )
    )

    save_alarms(alarms)

    print("Alarm added")


def list_alarms():
    alarms = load_alarms()

    if not alarms:
        print("No alarms found")
        return

    for alarm in alarms:
        print(
            f"{alarm.id} | "
            f"{alarm.trigger_time} | "
            f"{alarm.label}"
        )


def delete_alarm(alarm_id):
    alarms = load_alarms()

    alarms = [
        alarm
        for alarm in alarms
        if alarm.id != alarm_id
    ]

    save_alarms(alarms)

    print("Alarm deleted")