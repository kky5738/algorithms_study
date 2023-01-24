import sys
from math import ceil
import time

# it maybe occur timeout
def solution():
    
    m, n = map(int, sys.stdin.readline().rstrip().split(' '))
    start = time.time()
    prime_number = []

    for x in range(m, n+1):
        if x == 1: continue
        for i in range(2, ceil(x**0.5)+1):
            if x % i == 0:
                break
        else:
            prime_number.append(x)
    
    for j in prime_number:
        print(j)
    print(time.time() - start)

if __name__ == '__main__':
    solution()