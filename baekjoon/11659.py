# 누적합
# 구간 합 구하기 4 BOJ 11659

import sys
input = lambda : sys.stdin.readline()

n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]

for idx, x in enumerate(map(int, input().split())):
    arr[idx+1] = x + arr[idx]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])