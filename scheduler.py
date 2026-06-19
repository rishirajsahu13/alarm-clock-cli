import time
from datetime import datetime, timedelta
from storage import load_alarms, save_alarms
import threading

from storage import (
    load_alarms,
    save_alarms
)


def trigger_alarm(alarm, timeout=10):
    print("\n")
    print("=" * 40)
    print(f"ALARM: {alarm.label}")
    print("=" * 40)
    print("\a")

    print("\nOptions:")
    print("[s] Snooze 5 minutes")
    print("[d] Dismiss")
    print(f"(Auto-dismiss in {timeout} seconds)")

    result = {"choice": None}

    def get_input():
        try:
            result["choice"] = input("Choose: ").strip().lower()
        except:
            result["choice"] = None

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    thread.join(timeout)

    if result["choice"] is None:
        print("No input received → auto dismiss")
        return "d"

    return result["choice"]

def snooze_alarm(trigger_time, minutes=5):
    return (trigger_time + timedelta(minutes=minutes)).isoformat()

def run_scheduler():
    print("Scheduler running")

    while True:
        alarms = load_alarms()

        now = datetime.now()

        changed = False

        for alarm in alarms[:]:

            trigger_time = datetime.fromisoformat(alarm.trigger_time)

            # print current time and alarm for debugging
            print(f"Alarm ID: {alarm.id}, Label: {alarm.label}, Repeat Daily: {alarm.repeat_daily}")
            print(f"Current time: {now.isoformat()}, Alarm time: {trigger_time.isoformat()}")
            print(f"**************************")

            if now >= trigger_time:

                choice = trigger_alarm(alarm, timeout=10)

                # =========================
                # SNOOZE LOGIC ADDED HERE
                # =========================
                if choice == "s":
                    # move alarm 5 minutes from now
                    alarm.trigger_time = snooze_alarm(trigger_time, minutes=5)
                    changed = True

                elif choice == "d":
                    if alarm.repeat_daily:
                        # push to next day
                        next_time = trigger_time + timedelta(days=1)
                        alarm.trigger_time = next_time.isoformat()
                    else:
                        alarms.remove(alarm)
                    changed = True

                else:
                    print("Invalid choice, dismissing alarm.")
                    if alarm.repeat_daily:
                        next_time = trigger_time + timedelta(days=1)
                        alarm.trigger_time = next_time.isoformat()
                    else:
                        alarms.remove(alarm)
                    changed = True

        if changed:
            save_alarms(alarms)

        time.sleep(1)