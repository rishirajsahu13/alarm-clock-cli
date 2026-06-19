import argparse
from scheduler import run_scheduler

from cli import (
    add_alarm,
    list_alarms,
    delete_alarm
)

def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--time", required=True)
    add_parser.add_argument("--label", default="Alarm")
    add_parser.add_argument(
        "--daily",
        action="store_true"
    )

    subparsers.add_parser("list")
    subparsers.add_parser("run")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id")

    args = parser.parse_args()

    if args.command == "add":
        add_alarm(
            args.time,
            args.label,
            args.daily
        )

    elif args.command == "list":
        list_alarms()

    elif args.command == "delete":
        delete_alarm(args.id)

    elif args.command == "run":
        run_scheduler()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()