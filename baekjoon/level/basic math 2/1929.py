# 백준 1929번 소수 구하기
import sys
from math import ceil

# it maybe occur timeout -> 간신히 품.. eratos 이용해서 시간단축 가능할듯
def solution():
    
    m, n = map(int, sys.stdin.readline().rstrip().split(' '))
    prime_number = []

    for x in range(m, n+1):
        if x == 1: continue
        for i in range(2, ceil(x**0.5)+1):
            if x % i == 0 and x != i:
                break
        else:
            prime_number.append(x)
    
    for j in prime_number:
        print(j)

if __name__ == '__main__':
    solution()