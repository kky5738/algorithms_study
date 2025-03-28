# BOJ 1788 피보나치 수의 확장

import sys

MOD = 1000000000

def negative_fibo(x):
    prev_fibo = 0
    idx = 0
    next1 = 0
    next2 = 1
    flag = 0
    while True:
        if idx == x: return flag, abs(prev_fibo) % MOD
        flag = -1 if next1 > next2 else 1
        
        # 처음엔 양수와 동일하게 prev_fibo % MOD를 했으나 음수일 경우 값이 이상해짐.
        # 찾아보니 파이썬 % 연산은 항상 분모와 같은 기호를 반환..
        # 그러므로 fibo의 부호를 나타내는 flag를 MOD와 곱해 분자와 분모의 부호를 일치
        prev_fibo = (next2 - next1) % (MOD * flag) 
        
        next2, next1 = next1, prev_fibo
        idx -= 1
    
def positive_fibo(x):
    if x == 0: return 0, 0
    elif x == 1: return 1, 1
    
    next_fibo = 0
    idx = 0
    prev2 = 0
    prev1 = 1
    flag = 1
    while True:
        if idx == x - 1: return flag, next_fibo
        next_fibo = (prev1 + prev2) % MOD
        prev2, prev1 = prev1, next_fibo
        idx += 1
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    flag, fibo = positive_fibo(n) if n >= 0 else negative_fibo(n)
    print(flag)
    print(fibo)