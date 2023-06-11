# 백준 단계별로 풀기 1차원 배열 8번? 10810번 공 넣기

n, m = map(int, input().split())

result = ['0' for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for id in range(i, j+1):
        result[id-1] = str(k)

print(' '.join(result))