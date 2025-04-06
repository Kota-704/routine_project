from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

def get_next_date(start_date:date, period: int | None) -> date | None:
  today = date.today()
  if period is None:
    return start_date if start_date >= today else None

  current = start_date
  if period % 30 == 0 and period < 365:
    months = period // 30
    while current < today:
       current += relativedelta(months=months)
    return current
  elif period % 365 == 0:
    years = period // 365
    while current < today:
      current += relativedelta(years=years)
    return current
  else:
    while current < today:
      current += timedelta(days=period)
    return current

def get_days_left(next_date: date) -> int:
  return (next_date - date.today()).days
