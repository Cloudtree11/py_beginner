
from datetime import datetime

def count(d_begin, d_end, total, income):
    dt_begin = datetime.strptime(d_begin, "%Y-%m-%d")
    if d_end == 'now':
        dt_end = datetime.now()
    else:
        dt_end = datetime.strptime(d_end, "%Y-%m-%d")
    total += income
    day_count = (dt_end - dt_begin).days
    day_rate = 0.04 / 365

    for i in range(day_count):
        total = total + total * day_rate

    return total

base = 18500

# Begin at 2016-07-01
total = count("2016-07-01", "2017-07-05", base, 0)
# 2017-07-05 +1000
total = count("2017-07-05", "2017-10-30", total, 1000)
# 2017-10-30 +4295
total = count("2017-10-30", "2017-11-15", total, 4295)
# 2017-11-15 -4200
total = count("2017-11-15", "2018-04-08", total, -4200)
# 2018-04-08 +1000
total = count("2018-04-08", "2018-05-15", total, 1000)
# 2018-05-15 -1235
total = count("2018-05-15", "now", total, -1235)

print "sum is %.2f" % total

