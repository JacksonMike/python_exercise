def repair(n, a, b):
    pass


def s(n):
    a = list()
    for i in n:
        a.append(i)
    j = len(n) - 1
    while j > len(n) / 2:
        if n[j] == n[j - 1]:
            a.remove(n[j])
            break
        j -= 1
    for k in a:
        print(k, end="")


print("=")


def s(n):
    while n > 0:
        print("hell0")
        n -= 1


s(3)
