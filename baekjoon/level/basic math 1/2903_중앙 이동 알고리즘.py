# 백준 2903번 중앙 이동 알고리즘

import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    answer = (2**n + 1)**2
    print(answer)
        
    
if __name__ == '__main__':
    solution()
    