#-*- coding: utf-8 -*-
# by Yipeng Zhang

from time import clock


N = 10
step = 4
temp = {}

def move(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    count = 0
    for i in range(1, step+1):
        for j in range(1, step+1):
            count += move(a+i, b-j)
    return count


def move2(a, b):
    if (a, b) in temp:
        return temp[(a, b)]
    if a > b:
        temp[(a, b)] = 0
        return 0
    elif a == b:
        temp[(a, b)] = 1
        return 1
    count = 0
    for i in range(1, step+1):
        for j in range(1, step+1):
            count += move2(a+i, b-j)
    temp[(a, b)] = count
    return temp[(a, b)]


clock()

# print(move2(0, N))
# print(clock())


# print(move(0, N))
# print(clock())