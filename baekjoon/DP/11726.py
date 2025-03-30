# BOJ 11726 2xn 타일링
import sys

MOD = 10007

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    prev2 = 1
    prev1 = 2
    current = n
    
    for i in range(n-2):
        current = (prev2 + prev1) % MOD
        prev2, prev1 = prev1, current
    print(current)
    
if __name__ == "__main__":
    solution()