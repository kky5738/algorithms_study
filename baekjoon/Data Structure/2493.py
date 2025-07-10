import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split(" ")))

stack = []
result = []
count = 0

for index, value in enumerate(nums):
    while stack and stack[-1][1] < value:
        stack.pop()
    if stack:
        result.append(stack[-1][0])
    else:
        result.append(0)
    stack.append((index+1, value))
    
print(*result)