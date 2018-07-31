#/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime

def f(date):
    d = str(date.year) + "{:0>2}".format(str(date.month)) + "{:0>2}".format(str(date.day))
    b = bin(int(d))[2:]
    return b == b[::-1]

start = datetime.date(1964, 10, 10)
stop = datetime.date(2020, 7, 24)

while start != stop:
    if f(start):
        print(start.year, start.month, start.day)
    start += datetime.timedelta(days=1)