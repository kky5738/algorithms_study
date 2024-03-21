# 백준 / 단계별로 풀어보기 / 15. 약수, 배수와 소수 2 / 17103번 골드바흐 파티션
import sys
import math
import time

def get_primes(x: int) -> list:
    # 에라토스테네스의 체
    
    a = [False, False] + [True] * (x-1)

    for i in range(2, x+1):
        if a[i]:
            for j in range(i**2, x+1, i):
                a[j] = False
    
    return a

t = int(sys.stdin.readline().rstrip())
num = [0 for _ in range(t)]
for i in range(t):
    num[i] = (int(sys.stdin.readline().rstrip()))

primes = get_primes(max(num))
for i in range(t):
    cnt = 0
    
    # 27~30번 line 다른 사람 코드 참조
    for j in range(2, int(num[i]/2) + 1):

        if primes[j] and primes[num[i]-j]: 
            cnt += 1
    
    print(cnt)