# BOJ 1890 점프
import sys

def solution(n: int, graph: list[list[int]]) -> None:
    d = [[0 for _ in range(n)] for _ in range(n)]
    d[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            if d[i][j] == 0: continue
            
            x = graph[i][j]
            if i == n-1 and j == n-1: break
            
            if i + x < n:
                d[i+x][j] += d[i][j]
            if j + x < n:
                d[i][j+x] += d[i][j]
                
    print(d[n-1][n-1])
            
if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    solution(n, graph)