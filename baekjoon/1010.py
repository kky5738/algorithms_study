# 백준 1010 다리 놓기

d = [1] * 31
d[1] = 1

for i in range(2, 31):
    d[i] = d[i - 1] * i

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    answer = int(d[m] / (d[n] * d[m - n]))
    print(answer)
