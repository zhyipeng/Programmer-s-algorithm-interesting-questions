#/usr/bin/env python
#-*- coding: utf-8 -*-

n = 12

def move(l):
    global n
    if len(l) == n + 1:
        return 1
    count = 0
    for i in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
        next_p = [l[-1][0] + i[0], l[-1][1] + i[1]]
        if next_p not in l:
            count += move(l+[next_p])
    return count

print(move([[0, 0]]))