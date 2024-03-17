# 백준_단계별로 풀어보기_14. 집합과 맵_1269번 대칭 차집합
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
A = set(sys.stdin.readline().rstrip().split())
B = set(sys.stdin.readline().rstrip().split())

answer = (A | B) - (A & B)

print(len(answer))