from datetime import datetime, timedelta

#1
current_date = datetime.now().date()
print(current_date - timedelta(5))

#2
yesterday = current_date - timedelta(1)
tomorrow = current_date + timedelta(1)
print(yesterday)
print(current_date)
print(tomorrow)

#3
now_without_microseconds = datetime.now().replace(microsecond=0)
print(now_without_microseconds)

#4
date1 = datetime(2023, 1, 1, 12, 0, 0)
date2 = datetime(2023, 1, 2, 12, 0, 0)
difference = (date2 - date1).total_seconds()
print(difference)
