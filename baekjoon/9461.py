# BOJ 9461 파도반 수열

import sys

def solution():
    d = [1] * 101
    d[4] = 2
    d[5] = 2
    
    for i in range(6, 101):
        d[i] = d[i-1] + d[i-5]
    
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        print(d[n])
    

if __name__ == "__main__":
    solution()