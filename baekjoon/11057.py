# 백준 오르막 수 11057

import sys

n = int(sys.stdin.readline().rstrip())
MOD = 10007

dp = [[0] * 10 for _ in range(n + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0]  # j=0 초기화
    for j in range(1, 10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD  # 누적합 사용

print(sum(dp[n]) % MOD)