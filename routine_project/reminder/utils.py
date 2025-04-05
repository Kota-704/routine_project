from datetime import date, timedelta

def get_next_date(start_date:date, period: int | None) -> date | None:
  today = date.today()
  if period is None:
    return start_date if start_date >= today else None

  current = start_date
  while current < today:
    current += timedelta(days=period)
    return current

def get_days_left(next_date: date) -> int:
  return (next_date - date.today()).days
