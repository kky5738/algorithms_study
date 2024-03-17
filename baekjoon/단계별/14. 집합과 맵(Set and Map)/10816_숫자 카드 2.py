# 백준_단계별로 풀어보기_14. 집합과 맵_10816번 숫자 카드 2
import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target = list(map(int, sys.stdin.readline().rstrip().split()))

counter = Counter(num)

for x in target:
    print(counter[x], end=' ')