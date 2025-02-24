# 백준 9625 BABBA
k = int(input())

d = [(1, 0)] * (k + 1)
d[1] = (0, 1)

for i in range(2, k + 1):
    A = d[i - 1][0] + d[i - 2][0]
    B = d[i - 1][1] + d[i - 2][1]
    d[i] = (A, B)

print(d[k][0], d[k][1])