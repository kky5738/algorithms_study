import sys
from math import ceil

def solution():
    n = int(sys.stdin.readline().rstrip())
    num = [i for i in range(1, n+1)]
    prime_list = []

    for x in num:
        if x == 1: continue

        for i in range(2, ceil(x**0.5)+1):
            prime = 1
            if x % i == 0 and x != i:
                prime = 0
                break
        if prime == 1:
            prime_list.append(x)
    
    result = []
    idx = 0
    while True:
        
        if n in prime_list:
            result.append(int(n))
            break
                
        n = n/prime_list[idx]
        result.append(prime_list[idx])
        idx += 1
    print(result)

if __name__ == '__main__':
    solution()