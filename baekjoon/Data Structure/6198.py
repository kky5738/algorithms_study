# BOJ 6198 옥상 정원 꾸미기
import sys
input = lambda : sys.stdin.readline()

n = int(input())
heights = [int(input()) for _ in range(n)]

result = 0
stack = []

for current in heights:
    while stack and stack[-1] <= current:
        stack.pop()
        
    result += len(stack)
    stack.append(current)
    
print(result)