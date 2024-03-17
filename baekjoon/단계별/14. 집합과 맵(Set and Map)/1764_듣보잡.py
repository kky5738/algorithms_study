# 백준_단계별로 풀어보기_14. 집합과 맵_1764번 듣보잡
import sys

n, m = map(int, sys.stdin.readline().split())

arr1 = set()
for _ in range(n):
    arr1.add(sys.stdin.readline().rstrip())

arr2 = set()
for _ in range(m):
    arr2.add(sys.stdin.readline().rstrip())
    
answer = sorted(list(arr1 & arr2))
print(len(answer))

for name in answer:
    print(name)