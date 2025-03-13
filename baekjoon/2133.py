# BOJ 2133 타일 채우기
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    if n == 1: return print(0)
    
    d = [0] * (n+1)
    d[0] = 1
    d[2] = 3
    
    for i in range(4, n+1, 2):
        d[i] = 3 * d[i-2] + (d[i-2]-d[i-4])
        
    print(d[n])

if __name__ == "__main__":
    solution()