import sys

n, m = map(int, sys.stdin.readline().split())

user_info = dict([sys.stdin.readline().strip().split() for _ in range(n)])
find = [sys.stdin.readline().strip() for _ in range(m)]

for x in find:
    print(user_info[x])