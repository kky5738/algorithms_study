# BOJ 2156 포도주 시식
import sys

def solution(n: int, wine:list[int]):
    d = [0] * (n+1)
    d[1] = wine[0]
    d[2] = wine[0] + wine[1]
    
    for i in range(3, n+1):
        d[i] = max(d[i-2] + wine[i-1], d[i-3] + wine[i-2] + wine[i-1], d[i-1])
        
    print(d[n])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    wine = [int(input().rstrip()) for _ in range(n)]
    
    if n < 3:
        print(sum(wine))
        sys.exit(0)
        
    solution(n, wine)