#-*- coding: utf-8 -*-
# by Yipeng Zhang

from itertools import combinations

def isSimple(l):
    return len(l) == 2 * sum(l)

def canSimple(l):
    for i in range(30):
        if isSimple(l[:i+1]) and isSimple(l[i+1:]):
            return True
    return False

# 0表示男，1表示女
# l0 = [0 if i<21 else 1 for i in range(31)]
# d0 = {key: value for key, value in enumerate(l0)}
# l0 = [0 for i in range(30)]
# count = 0
# for c in combinations(range(30), 10):
#     for k in c:
#         l0[k] = 1
#     if not canSimple(l0):
#         count += 1
#     l0 = [0 for i in range(30)]
#
#     print(count)

boy = 21
girl = 11

l = [[0 for j in range(boy)] for i in range(girl)]

l[0][0] = 1
for i in range(girl):
    for j in range(boy):
        if i != j and (boy-j) != (girl-i):
            if j > 0:
                l[i][j] += l[i][j-1]
            if i > 0:
                l[i][j] += l[i-1][j]

print(l[girl-2][boy-1] + l[girl-1][boy-2])

# c = 0
# def f1(a, b):
#     if a == 0 or b == 0:
#         return 1
#     else:
#         global c
#         c += 1
#         print(c)
#         return f1(a-1, b) + f1(a, b-1)
#
#
# print(f1(20, 10))