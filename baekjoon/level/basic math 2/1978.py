import sys
from math import ceil

def solution():
    n = int(sys.stdin.readline().rstrip())
    input = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    result = 0
    
    for num in input:
        if num == 1: 
            result += 1
            continue
        
        for i in range(2, ceil(num**0.5)+1):
            if num % i == 0 and num != i:
                result += 1
                break

    print(n - result)

if __name__ == '__main__':
    solution()