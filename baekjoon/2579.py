# BOJ 2579 계단 오르기
import sys

def solution(n: int, stairs: list):
    d = [0] * (n+1)
    d[1] = stairs[1]
    d[2] = d[1] + stairs[2]
    
    for i in range(3, n+1):
        d[i] = max(d[i-2] + stairs[i], d[i-3] + stairs[i-1] + stairs[i])
    
    return d[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    stairs = [0]
    for _ in range(n):
        stairs.append(int(input().rstrip()))
    if n < 3:
        print(sum(stairs))
        sys.exit(0)
    result = solution(n, stairs)
    print(result)