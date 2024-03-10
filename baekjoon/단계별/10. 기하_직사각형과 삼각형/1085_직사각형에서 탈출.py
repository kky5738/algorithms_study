# 백준 1085번 직사각형에서 탈출

import sys

def solution():
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split(' '))
    
    a = abs(h-y) if abs(h-y) < abs(0-y) else abs(0-y)
    b = abs(w-x) if abs(w-x) < abs(0-x) else abs(0-x)
    
    answer = a if a < b else b
    print(answer)

if __name__ == '__main__':
    solution()