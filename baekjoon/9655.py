# 백준 9655 돌 게임

n = int(input())
d = [0]
d += ['SK' if i % 2 == 0 else 'CY' for i in range(n)]

print(d[n])