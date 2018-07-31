target = 1000
count = 0
for i in range(15):
    for j in range(15):
        for k in range(15):
            for l in range(15):
                if 10*i + 50*j + 100*k + 500*l == 1000 and i+j+k+l <=15:
                    count += 1
print(count)

