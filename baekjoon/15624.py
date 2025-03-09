# BOJ 15624 피보나치 수 7

def solution():
    import sys

    MOD = 1000000007
    n = int(sys.stdin.readline().rstrip())
    if n < 2:
        print(n % MOD)
        return
    
    prev2 = 0
    prev1 = 1
    idx = n
    next_fib = 0
    
    while idx > 1:
        next_fib = (prev1 + prev2) % MOD  # 메모리 절약을 위해 모듈러 연산 적용한 값을 저장
        prev2, prev1 = prev1, next_fib
        idx -= 1
    
    print(next_fib % MOD)

if __name__ == "__main__":
    solution()