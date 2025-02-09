a = [2, 1, 5, 4, 3, 7]

for i in range(len(a)):
    small = i
    for j in range(i, len(a)):
        if a[small] > a[j]:
            small = j
    a[i], a[small] = a[small], a[i]
print(a)