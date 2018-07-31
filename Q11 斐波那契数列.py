#-*- coding: utf-8 -*-
# by Yipeng Zhang

def Fib(n):
    i = 0
    a = 0
    b = 1
    while i < n:
        yield b
        a, b = b, a + b
        i += 1

def sum_all(n):
    return sum((int(i) for i in str(n)))

count = 0
for n in Fib(111):
    if count == 5:
        break
    if n > 144 and n % sum_all(n) == 0:
        count += 1
        print(n)