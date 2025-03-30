# BOJ 1904 01타일
import sys

MOD = 15746

def solution():
    n = int(sys.stdin.readline().rstrip())

    if n < 3: return print(n)
    
    prev2 = 1
    prev1 = 2
    current = 0

    for _ in range(n-2):
        current = (prev2 + prev1) % MOD
        prev2, prev1 = prev1, current
        
    print(current)

if __name__ == "__main__":
    solution()