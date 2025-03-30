# BOJ 1003 피보나치 함수
import sys

def solution():
    d = [1] * 43
    d[42] = 0
    
    for i in range(2, 41):
        d[i] = d[i-2] + d[i-1]
        
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        print(d[n-2], d[n-1])

if __name__ == "__main__":
    solution()