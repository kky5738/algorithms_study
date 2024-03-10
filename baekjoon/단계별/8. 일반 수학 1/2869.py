import sys
from math import ceil

def solution():
    a, b, v = map(int, sys.stdin.readline().rstrip().split(' '))
    
    d = a - b
    n = ((v - a) / d) + 1
    answer = ceil(n)
    print(answer)

if __name__ == '__main__':
    solution()