# 백준 11727 2xn 타일링 2, 첫번째 풀이 시도는 실패, 며칠 뒤 질문게시판에 1~12의 출력 값 보고 점화식 유추 성공

import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n + 1)
d[1] = 1
arr = [1, -1]

for i in range(2, n+1):
    d[i] = (2*d[i-1] + arr[i % 2]) % 10007

print(d[n] % 10007)

# GPT가 올바른 점화식으로 최적화 해준 코드. 위 코드는 불필요한 보정이 들어갔고 점화식이 부정확함.
def solution():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    if n == 1:
        print(1)
        return
    elif n == 2:
        print(3)
        return

    prev2, prev1 = 1, 3  # d[1] = 1, d[2] = 3

    for _ in range(3, n + 1):
        current = (prev1 + 2 * prev2) % 10007
        prev2, prev1 = prev1, current

    print(prev1)