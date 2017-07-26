
from datetime import datetime

base = 18500
dt_begin = datetime.strptime("2016-07-01", "%Y-%m-%d")
# 2017-07-05 +1000
dt_end = datetime.strptime("2017-07-05", "%Y-%m-%d")
day_count = (dt_end - dt_begin).days
day_rate = 0.04 / 365
total = base

for i in range(day_count):
    total = total + total * day_rate

dt_now = datetime.now()
total += 1000
day_count = (dt_now - dt_end).days

for i in range(day_count):
    total = total + total * day_rate


print "day count is", day_count
print "sum is %.2f" % total
