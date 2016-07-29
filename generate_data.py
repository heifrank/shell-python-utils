#!/usr/bin/python

import sys
import datetime

if len(sys.argv) != 3:
    print 'argv num must be 3'
    print 'usage python xxx.py 2016-07-12 num_of_line'
    sys.exit(1)

from_day_str = sys.argv[1]
num_per_line = int(sys.argv[2])

from_date = datetime.datetime.strptime(from_day_str, "%Y-%m-%d")

today = datetime.datetime.now()

gap_days = (today - from_date).days



# print from_date.strftime("%Y%m%d")
# print gap_days

cnt = 0
days = []
for i in range(gap_days):
    cnt += 1
    days.append( (from_date + datetime.timedelta(days = i)).strftime("%Y%m%d") )
    if cnt % num_per_line == 0:
        print '%s' % ','.join(days)
        days = []

if len(days) != 0:
    print '%s' % ','.join(days)


