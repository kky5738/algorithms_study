import sys
import math

def solution():
    n = int(sys.stdin.readline().rstrip())
    sum = 0

    for i in range(1, n):
        if sum < n:
            sum += i
            continue
        level = i - 1
        strat = sum - level + 1
        print(level, i, strat)
        for j in range(level, 0, -1):
            # sum = 1+2+3+4 < num continue 대충 이런 식
            pass

        break

        
    
    pass

if __name__ == '__main__':
    solution()

"""
1 = 1*1
2 = 
"""