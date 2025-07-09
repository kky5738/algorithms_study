import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split(" ")))

stack = []
result = []
count = 0

for index, value in enumerate(nums):
    current = value
    
    if not stack:
        result.append(0)
    else:
        if stack[-1][1] < current: # 수신 탑 찾기
            while stack and stack[-1][1] <= current:
                stack.pop()
            
            if stack:
                result.append(stack[-1][0] + 1)
            else:
                result.append(index)
        else:
            result.append(index)
    stack.append((index, current))
    
print(*result)