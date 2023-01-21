import sys
from math import ceil

def solution():
    m = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    num = [i for i in range(m, n+1)]
    result = []

    for x in num:
        if x == 1: continue

        for i in range(2, ceil(x**0.5)+1):
            prime = 1
            if x % i == 0 and x != i:
                prime = 0
                break
        if prime == 1:
            result.append(x)
        
    if not result:
        return print(-1)
        
    else:
        print(sum(result))
        print(min(result))

if __name__ == '__main__':
    solution()