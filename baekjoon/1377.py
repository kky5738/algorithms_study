# 백준 1377 버블 소트 # 시간초과..
import sys

n = int(sys.stdin.readline().rstrip())
A = [0] * (n + 1)
for k in range(1, n+ 1):
    A[k] = [int(sys.stdin.readline().rstrip())]

changed = False
for i in range(1, n + 1):
    changed = False
    for j in range(1, n - i):
        if A[j] > A[j + 1]:
            changed = True
            A[j], A[j + 1] = A[j + 1], A[j]
    if changed == False:
        print(i)
        break
