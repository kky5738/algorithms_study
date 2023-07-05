# 백준 1차원 배열 10813 공바꾸기

n, m = map(int, input().split())
array = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = array[i-1]
    array[i-1] = array[j-1]
    array[j-1] = temp

for k in range(n):
    print(array[k], end=' ')
