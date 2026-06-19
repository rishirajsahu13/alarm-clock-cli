from datetime import datetime, timedelta
from scheduler import snooze_alarm


def test_snooze_alarm_5_minutes():
    base_time = datetime(2026, 6, 19, 10, 0, 0)

    result = snooze_alarm(base_time, 5)

    expected = base_time + timedelta(minutes=5)

    assert result == expected.isoformat()


def test_snooze_alarm_default():
    base_time = datetime(2026, 6, 19, 10, 0, 0)

    result = snooze_alarm(base_time)

    expected = base_time + timedelta(minutes=5)

    assert result == expected.isoformat()