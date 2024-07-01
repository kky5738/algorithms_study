n, m = map(int, input().split())
money = [0] * n
for i in range(n):
    money[i] = int(input())

d = [-1] * (m + 1)

d[money[0]-1] = 1

for i in range(money[0], m + 1):
    for c in money:
        if i % c == 0: # 조건문을 안써도 되지 않을까?
            d[i] = min(i // c, d[i-c] + 1)
            break
        
print(d[m])