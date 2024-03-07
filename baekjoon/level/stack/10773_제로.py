# 백준 단계별로 풀기_스택, 큐, 덱_10773번 제로
import sys

k = int(sys.stdin.readline().rstrip())

answer = []

for i in range(k):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        answer.pop()
    else:
        answer.append(x)

print(sum(answer))