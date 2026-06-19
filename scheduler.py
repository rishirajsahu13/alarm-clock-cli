import time
from datetime import datetime, timedelta

from storage import (
    load_alarms,
    save_alarms
)


def trigger_alarm(alarm):
    print("\n")
    print("=" * 40)
    print("ALARM")
    print(alarm.label)
    print("=" * 40)

    print("\a")


def run_scheduler():
    print("Scheduler running")

    while True:
        alarms = load_alarms()

        now = datetime.now()

        changed = False

        for alarm in alarms[:]:

            trigger_time = datetime.fromisoformat(
                alarm.trigger_time
            )

            #print current time and alarm for debugging
            print(f"Alarm ID: {alarm.id}, Label: {alarm.label}, Repeat Daily: {alarm.repeat_daily}")
            print(f"Current time: {now.isoformat()}, Alarm time: {trigger_time.isoformat()}")

            if now >= trigger_time:

                trigger_alarm(alarm)

                if alarm.repeat_daily:

                    next_time = (
                        trigger_time
                        + timedelta(days=1)
                    )

                    alarm.trigger_time = (
                        next_time.isoformat()
                    )

                    changed = True

                else:
                    alarms.remove(alarm)
                    changed = True

        if changed:
            save_alarms(alarms)

        time.sleep(1)