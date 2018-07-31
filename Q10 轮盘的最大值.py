#-*- coding: utf-8 -*-
# by Yipeng Zhang

Eur = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
Ama = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
# print(len(Eur), len(Ama))

Eur1 = Eur + Eur
Ama1 = Ama + Ama

count = 0
for n in range(2, 37):
    i = 0
    j = i + n - 1
    sum_e = 0
    sum_a = 0
    temp1 = sum(Eur1[0:j+1])
    temp2 = sum(Ama1[0:j+1])
    while i < len(Ama):
        sum_e = max(sum_e, temp1)
        sum_a = max(sum_a, temp2)
        temp1 = temp1 - Eur1[i] + Eur1[j+1]
        temp2 = temp2 - Ama1[i] + Ama1[j+1]
        i += 1
        j += 1
    if sum_e < sum_a:
        count += 1
print(count)