# BOJ 17298 오큰수
# 뒤에서부터 봐야 한다는 GPT 도움 받음..
import sys
input = lambda : sys.stdin.readline()

n = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n-1, -1, -1):
    current = arr[i]
    while stack and stack[-1] <= current:
        stack.pop()
    
    if stack:
        result[i] = stack[-1]
    else:
        result[i] = -1
        
    stack.append(current)

print(*result)