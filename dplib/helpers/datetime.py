import time
from datetime import datetime, timedelta, timezone


def add_timezone_infromation(naive: str):
    # Parse the datetime string into a naive datetime object
    dt_naive = datetime.fromisoformat(naive)

    # Get the local timezone offset in seconds
    local_offset_sec = -time.timezone if time.localtime().tm_isdst == 0 else -time.altzone

    # Convert the offset to a timezone object
    local_timezone = timezone(timedelta(seconds=local_offset_sec))

    # Assign the local timezone to the naive datetime object
    dt_aware = dt_naive.replace(tzinfo=local_timezone)

    # Serialize to ISO 8601 format
    aware = dt_aware.isoformat()

    return aware
