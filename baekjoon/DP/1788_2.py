import sys

# 모듈러
MOD = 1000000000
input = sys.stdin.readline

def solution(n: int) -> None:
    if abs(n) < 2:
        print(abs(n))
        print(abs(n))
        return
    
    prev1, prev2 = 1, 0
    
    for _ in range(abs(n)-1):
        current = (prev1 + prev2) % MOD
        prev1, prev2 = current, prev1
    
    print(-1 if n < 0 and n % 2 == 0 else 1) # 삼항연산자
    print(current % MOD)

if __name__ == "__main__":
    n = int(input().rstrip())
    
    solution(n)