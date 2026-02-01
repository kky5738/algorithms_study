import sys
input = sys.stdin.readline

n = int(input())
a_list = set(map(int, input().split()))

m = int(input())
data = list(map(int, input().split()))
set_data = set(data)

intersection = a_list.intersection(set_data)

for i in data:
    if i in intersection:
        print(1)
    else:
        print(0)