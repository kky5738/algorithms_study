# 백준 2903번 중앙 이동 알고리즘

import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    print(9 * (4**(n-1)) - ((4**(n-1)) * 2 + 4**(n-2)))
    print(9 * (4**(n-1)))
    print(4**0)
if __name__ == '__main__':
    solution()
    
    """
    
    0 4 1
    1 9 4
    2 25(36) 16
    3 9*16
    
    4 1 
    9 4
    25 16
    """