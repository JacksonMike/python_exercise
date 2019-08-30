import random


def matrix(n):
    m = []
    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            tmp.append(random.randint(0, 10))
        m.append(tmp)
    return m


def brute_force(n):
    a = matrix(n)
    b = matrix(n)
    c = matrix(n)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            c[i][j] = 0
            for k in range(0, n, 1):
                c[i][j] += a[i][k] * b[k][j]
    return c


print(brute_force(100))
