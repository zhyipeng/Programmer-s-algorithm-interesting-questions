#-*- coding: utf-8 -*-
# by Yipeng Zhang

import copy

def search(country, country_list, length):
    next_country = [i for i in country_list if country[-1]==i[0]]
    if len(next_country) > 0:
        c = next_country.pop()
        search(c, country_list, length+1)
    else:
        global max_country
        return max(max_country, length)

def search_dfs(country, country_d, length):
    mark(country_d, country)
    if country[-1] not in country_d:
        return 0
    for c in country_d[country[-1]]:
        if c[0] == '0':
            continue
        else:
            search_dfs(country, country_d, length+1)
    return max(max_country, length)

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



def bfs(country, country_d, max_country):
    print(country)
    res = [max_country]

    temp = []
    st = []
    st.append(country)
    while st != []:
        now = st.pop()
        # print(country_d)
        print(st)
        # print(now)
        if now[-1] not in country_d:
            res.append(len(st) + 1)
            # print(st + [now])
            continue
        for c in country_d[now[-1]]:
            # if c[0] == '0':
            #     continue
            if len(temp) <= len(st):
                temp = st[:] + [now]
            else:
                if temp[len(st)] != now:
                    temp = st[:] + [now]
                    break
            # print(st)
            print(temp)
            if c in temp or c in st:
                continue
            else:
                # nx = c
                st.append(now)
                # mark(country_d, c)
                st.append(c)
                break
        else:
            res.append(len(st) + 1)
            # print(st + [now])
    print(max(res))
    return max(res)











with open('country_list.txt', 'r') as f:
    country_list = f.readlines()

country_list = list(map(lambda c: c[:-1].upper(), country_list))
country_dict = {}
for i in country_list:
    if i[0] in country_dict:
        country_dict[i[0]] += [i]
    else:
        country_dict[i[0]] = [i]


# print(country_list)

max_country = 1

# for c in country_list:
#     # max_country = search(c, country_list, max_country)
#     # print(country_d)
#     # max_country = search_dfs(c, country_d, max_country)
#     max_country = bfs(c, country_dict, max_country)
country = 'CAMEROON'
bfs(country, country_dict, max_country)

print(max_country)


