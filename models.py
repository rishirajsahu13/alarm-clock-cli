from dataclasses import dataclass


@dataclass
class Alarm:
    id: str
    trigger_time: str
    label: str
    repeat_daily: bool = False