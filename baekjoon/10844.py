# 백준 10844 쉬운 계단 수, 이것도 점화식 못구해서 ChatGPT 도움 받음..

def solution():
    ''' GPT가 준 힌트.
    DP 테이블 정의

    dp[i][j]: 길이가 i이고 마지막 숫자가 j인 계단 수의 개수
    예를 들어, dp[2][1]은 길이가 2이고 끝자리가 1인 계단 수의 개수를 의미
    점화식 세우기

    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    단, j = 0이면 dp[i-1][-1]은 존재하지 않으므로 dp[i][0] = dp[i-1][1]
    j = 9이면 dp[i-1][10]은 존재하지 않으므로 dp[i][9] = dp[i-1][8]
    초기값 설정

    dp[1][1]부터 dp[1][9]까지는 각각 1 (1자리 숫자는 자기 자신만 가능)
    dp[1][0] = 0 (0으로 시작하는 수는 계단수가 아님)
    결과 출력

    dp[N][0]부터 dp[N][9]까지의 합을 1,000,000,000으로 나눈 나머지 출력
    '''
    import sys
    n = int(sys.stdin.readline().rstrip())

    d = [[0]*10 for _ in range(n + 1)]

    for j in range(1, 10):
        d[1][j] = 1

    for i in range(2, n+1):
        d[i][0] = d[i-1][1]
        d[i][9] = d[i-1][8]
        for j in range(1, 9):
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
            

    print(sum(d[n]) % 1000000000)

def solution():
    """GPT가 개선해준 코드
    """
    import sys
    n = int(sys.stdin.readline().rstrip())

    d = [[0]*10 for _ in range(n + 1)]

    for j in range(1, 10):
        d[1][j] = 1

    for i in range(2, n + 1):
        d[i][0] = d[i-1][1] % 1000000000
        d[i][9] = d[i-1][8] % 1000000000
        for j in range(1, 9):
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % 1000000000

    print(sum(d[n]) % 1000000000)
    
if __name__ == "__main__":
    solution()