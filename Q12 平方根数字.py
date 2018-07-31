#-*- coding: utf-8 -*-
# by Yipeng Zhang

from math import sqrt, modf

def only_float(n):
    x, z = modf(sqrt(n))
    x = str(x)[2:12]
    return len(set(x)) == 10

def all_num(n):
    n = str(sqrt(n))[:11]
    return len(set(n)) == 11


# print(only_float(143))

n = 1
a = 0
b = 0
while 1:
    if a == 0:
        if only_float(n):
            a = n
    if b == 0:
        if all_num(n):
            b = n
    if a and b:
        break
    n += 1
    # print(n)
print(b, a)
