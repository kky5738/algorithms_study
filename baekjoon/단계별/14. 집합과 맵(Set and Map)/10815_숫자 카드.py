# 백준_단계별로 풀어보기_14. 집합과 맵(Set and Map)_10815번 숫자 카드
import sys

n = int(sys.stdin.readline().rstrip())
cards = set(sys.stdin.readline().rstrip().split())

m = int(sys.stdin.readline().rstrip())
target = sys.stdin.readline().rstrip().split()

for i in range(m):
    print(int(target[i] in cards), end=' ')