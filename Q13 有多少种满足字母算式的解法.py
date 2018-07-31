#-*- coding: utf-8 -*-
# by Yipeng Zhang

import re
from itertools import permutations

def isTrue(d, exp):
    res = ''
    for ch in exp:
        if ch in d:
            res += str(d[ch])
        elif ch == '=':
            res += '=='
        else:
            res += ch
    return (eval(res))

def isRight(d, f):
    for i in f:
        if d[i] == 0:
            return False
    return True

exp = 'READ + WRITE + TALK = SKILL'
# exp = 'A + B = C'
num = re.split(r'[^a-zA-Z]+', exp)
w = list(set([i for i in exp if ('A'<=i<='Z')]))
first = list(set([i[0] for i in num]))
l_w = len(w)
d = {}
l = [i for i in range(l_w)]
count = 0
m = 0
for c in permutations(l, l_w):
    # print(m)
    # print(count)
    for i in range(l_w):
        d[w[i]] = c[i]
        m += 1

    if not isRight(d, first):
        continue
    else:
        if isTrue(d, exp):
            count += 1

print(count)
