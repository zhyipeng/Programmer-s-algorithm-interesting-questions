
def c(num):
    l = ['*', '']
    res = []
    n = str(num)
    for l1 in l:
        for l2 in l:
            for l3 in l:
                temp = n[0] + l1 + n[1] + l2 + n[2] + l3 + n[3]
                if len(temp) > 4:
                    res.append(temp)
    return res

for num in range(1000, 10000):
    m = int(str(num)[::-1])
    for i in c(num):
        try:
            temp = eval(i)
            if temp == m:
                print('%s=%d' % (i, num))
                break
        except:
            continue