import datetime

DOCTOR_STATE_LIST = [
    ("draft", "Draft"),
    ("active", "Active"),
    ("arch", "Arch"),
]

SHIFT_DURATION = [
    ("3", "3 Hours"),
    ("6", "6 Hours"),
    ("8", "8 Hours"),
]

STATE_LIST = [
    ("draft", "Draft"),
    ("created", "Created"),
    ("done", "Done"),
]

VISIT_TIME = datetime.timedelta(
    hours=00, minutes=30, seconds=00
)

delta = datetime.timedelta(seconds=1)