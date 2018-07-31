#-*- coding: utf-8 -*-
# by Yipeng Zhang

res = []
max_country = 1

def dfs(prev, max_d):
    # islast = True
    for i, c in enumerate(country_list):
        if c[0] == prev[-1]:
            if not isuse[i]:
                # islast = False
                isuse[i] = True
                dfs(c, max_d+1)
                isuse[i] = False
    # if 1:
    global max_country
    max_country = max(max_country, max_d)


def mark(cd, c):
    for i in cd:
        if c in cd[i]:
            for j in range(len(cd[i])):
                if c == cd[i][j]:
                    cd[i][j] = '0' + cd[i][j]

def remark(cd, c):
    for i in cd:
        for j in range(len(cd[i])):
            if cd[i][j][1:] == c:
                cd[i][j] = c

with open('country_list.txt', 'r') as f:
    country_list = f.readlines()

country_list = list(map(lambda c: c[:-1].upper(), country_list))
country_dict = {}
for i in country_list:
    if i[0] in country_dict:
        country_dict[i[0]] += [i]
    else:
        country_dict[i[0]] = [i]

# max_country = 1
isuse = [False for i in country_list]
for i, c in enumerate(country_list):
    isuse[i] = True
    dfs(c, 1)
    isuse[i] = False
print(max_country)