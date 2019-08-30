for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print(j, end=" ")
    print()
print("="*100)
for i in range(1, 7):
    for j in range(1, 7):
        if j <= 7-i:
            print(j, end=" ")
    print()
print("="*100)
for i in range(1, 7):
    for j in range(1, 7):
        if j < 7-i:
            print(" ", end=" ")
        else:
            print(7-j, end=" ")
    print()
print("="*100)
for i in range(1, 7):
    for j in range(1, 7):
        if j < i:
            print(" ", end=" ")
        else:
            print(j-i+1, end=" ")
    print()



