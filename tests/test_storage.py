from storage import save_alarms, load_alarms
from models import Alarm


def test_save_and_load(tmp_path, monkeypatch):
    test_file = tmp_path / "alarms.json"

    monkeypatch.setattr("storage.DATA_FILE", str(test_file))

    alarm = Alarm(
        id="test123",
        trigger_time="2026-06-19T10:00:00",
        label="Test",
        repeat_daily=False
    )

    save_alarms([alarm])

    loaded = load_alarms()

    assert len(loaded) == 1
    assert loaded[0].id == "test123"
    assert loaded[0].label == "Test"