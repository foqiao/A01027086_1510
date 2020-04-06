import datetime
import time

now = datetime.datetime.now()
print(type(now))
print(now)

presents = datetime.datetime(2018, 12, 25, 9, 0, 0)
print(presents.year, presents.month, presents.day, presents.hour, presents.minute, presents.second)
print(presents)

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time())) # need to import time

halloween = datetime.datetime(2018, 10, 31)
nyd = datetime.datetime(2019, 1, 1)
oct_31 = datetime.datetime(2018, 10, 31)
print(halloween == oct_31)
print(halloween > nyd)
print(nyd != oct_31)

delta = datetime.timedelta(days=9, hours=21, minutes=5, seconds=0)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))
print(presents.strftime('%Y/%m/%d'))