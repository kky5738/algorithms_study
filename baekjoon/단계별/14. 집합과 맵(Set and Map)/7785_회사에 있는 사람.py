# 백준_단계별로 풀어보기_14. 집합과 맵(Set and Map)_7785번 회사에 있는 사람
import sys

answer = set()

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    name, state = sys.stdin.readline().rstrip().split()
    if state == 'enter':
        answer.add(name)
    else:
        answer.discard(name)

answer = sorted(list(answer))

for i in range(len(answer)-1, -1, -1):
    print(answer[i])