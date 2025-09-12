import random
from datetime import datetime, timedelta

def random_datetime(start, end):
    """Generate a random datetime between 'start' and 'end'."""
    delta = end - startrandom_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds) # type: ignore

# Example usage
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2025, 12, 31, 23, 59, 59)

random_dt = random_datetime(start_date, end_date)
print(random_dt)