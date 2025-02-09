import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr += [list(sys.stdin.readline().split())]

arr = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(arr[i][0])