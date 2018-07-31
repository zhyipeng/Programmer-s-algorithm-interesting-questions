# 深度优先搜索

def cut(m, n, count):
    if count >= n:
        return 0
    elif count <= m:
        return 1 + cut(m, n, count*2)
    else:
        return 1 + cut(m, n, m + count)

print(cut(3, 20, 1))
print(cut(5, 100, 1))