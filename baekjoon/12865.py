# BOJ 12865 평범한 배낭, 다시 풀어보기
import sys

def solution(n: int, m: int, stuff: list[list[int]]):
    dp = [[0] * (m+1) for _ in range(n+1)]
        
    for i in range(1, n+1):
        w, v = stuff[i-1]  # i번째 물건의 무게, 가치
        for j in range(1, m+1):  # 배낭의 무게 1~m까지
            if j >= w:  # 물건을 넣을 수 있는 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:  # 물건을 넣을 수 없는 경우
                dp[i][j] = dp[i-1][j]

    print(dp[n][m])  # 최적해 출력

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n, m = map(int, input().rstrip().split())
    
    stuff = [list(map(int, input().rstrip().split())) for _ in range(n)]

    solution(n, m, stuff)