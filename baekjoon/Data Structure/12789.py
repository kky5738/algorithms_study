# # 틀린 코드
# import sys
# input = lambda : sys.stdin.readline()

# n = int(input())
# arr = list(map(int, input().split()))

# stack = []
# result = []
# idx = 1
# answer = ""

# while arr or stack:
#     x = arr.pop(0) if arr else stack.pop()
#     if x == idx:
#         result.append(x)
#         idx += 1
#     else:
#         if stack and stack[-1] < x:
#             print("Sad")
#             break
#         stack.append(x)
# else: # while문 안에서 break 만나지 않고 while을 빠져나올 경우
#     print("Nice")
    
# 아래는 gpt 코드
import sys
input = lambda : sys.stdin.readline()

n = int(input())
arr = list(map(int, input().split()))

stack = []
idx = 1

while arr:
    current = arr.pop(0)
    
    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1
    
    if current == idx:
        idx += 1
    else:
        stack.append(current)

# arr를 다 처리한 후에도 stack에 남은 게 있을 수 있음
while stack and stack[-1] == idx:
    stack.pop()
    idx += 1

print("Nice" if not stack else "Sad")