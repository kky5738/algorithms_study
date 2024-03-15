# 백준 단계별로 풀어보기_12.brute force_1436번 영화감독 숌
import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
answer = 666
while 1:
    if '666' in str(answer):
        cnt += 1
        if cnt == n:
            break
    answer += 1

print(answer)