# 백준 피보나치 수 2747

import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n + 1)
d[1] = 1

for i in range(2, n + 1):
    d[i] = d[i-1] + d[i-2]

print(d[n])