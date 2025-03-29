# BOJ 12865 평범한 배낭, 다시 풀어보기
import sys

def solution(n: int, m: int, stuff: list[list[int]]):
    dp = [[0] * (m+1) for _ in range(n+1)]
    stuff = sorted(stuff)
        
    for i in range(1, n+1):
        w, v = stuff[i-1]
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

    print(dp[n][m])

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n, m = map(int, input().rstrip().split())
    
    stuff = [list(map(int, input().rstrip().split())) for _ in range(n)]

    solution(n, m, stuff)