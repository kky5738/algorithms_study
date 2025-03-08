# BOJ 1660 캡틴 이다솜. 아직까진 DP 점화식 떠올리는게 쉽지 않음. 다양한 DP 문제를 접해보면 좀 나아질까? 아직은 몇문제 풀지도 않았으니...

# 내 접근. 누적된 대포 개수는 구했지만 이를 활용해 사면체 개수 구하는 방법을 떠올리지 못함
def solution():
    import sys

    n = int(sys.stdin.readline().rstrip())

    d = [0] * (n + 1)
    prev1 = 1
    d[1] = 1
    for i in range(2, n+1):
        current = prev1 + i
        d[i] = current + d[i-1]
        prev1 = current

def solution_from_gpt(): # GPT가 만들어줬어요
    import sys

    # 입력
    n = int(sys.stdin.readline().strip())

    # 1. 사면체 숫자 목록 생성
    tetra = []
    num = 1  # 현재 층
    value = 1  # 사면체 숫자
    while value <= n:
        tetra.append(value)
        num += 1
        value += num * (num + 1) // 2  # 누적 삼각수

    # 2. DP 초기화 (큰 값으로 설정)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 대포알 0개는 사면체 0개

    # 3. DP 테이블 채우기
    for t in tetra:
        for j in range(t, n + 1):
            dp[j] = min(dp[j], dp[j - t] + 1)

    # 4. 결과 출력
    print(dp[n])

if __name__ == "__main__":
    solution_from_gpt()