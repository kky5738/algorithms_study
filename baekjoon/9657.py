# BOJ 9657 돌 게임 3
import sys

def solution(n):
    d = [0] * (n+2) # 0: SK, 1: CY
    d[2] = 1
    
    for i in range(5, n+1):
        d[i] = not(d[i-4] + d[i-3] + d[i-1])
    return d[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    
    print("CY") if solution(n) else print("SK")