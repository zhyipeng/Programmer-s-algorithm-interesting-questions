#/usr/bin/env python
#-*- coding: utf-8 -*-

def kaolazi(n):
    m = 3 * n + 1
    while m != 1 and m != n:
        if m % 2 == 0:
            m = m // 2
        else:
            m = 3 * m + 1
    if m == n:
        return True
    elif m == 1:
        return False

count = 0
for i in range(0, 10000, 2):
    if kaolazi(i):
        count += 1
        print(i)
print(count)