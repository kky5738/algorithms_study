# 백준_단계별로 풀어보기_14. 집합과 맵(Set and Map)_14425번 문자열 집합
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

strings = set()
for _ in range(n):
    strings.add(sys.stdin.readline().rstrip())

answer = 0
for _ in range(m):
    answer += int(sys.stdin.readline().rstrip() in strings)

print(answer)