l = [0 for i in range(100)]
for i in range(1, 101):
    for j in range(100):
        if (j+1) % i == 0:
            if l[j]==0:
                l[j] = 1
            else:
                l[j] = 0
for i, v in enumerate(l):
    if v == 1:
        print(i+1, end=' ')
