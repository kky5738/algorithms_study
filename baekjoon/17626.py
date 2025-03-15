# BOJ 17626 Four Squrares
import sys

def solution(n:int) -> int:
    d = [0] * (n+1)
    d[1] = 1
    
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % int(i**0.5) == 0 and int(i**0.5) == i // int(i**0.5):
            d[i] = 1
            continue
        for j in range(2, int(i**0.5)+1):
            
            d[i] = min(d[i - j**2]+1, d[i])
    
    return d[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    
    answer = solution(n)
    print(answer)