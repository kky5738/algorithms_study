# BOJ 11048 이동하기
import sys

def solution(n:int, m:int, graph:list[int]):
    d = [[0 for _ in range(m+1)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1]) + graph[i][j]
    
    print(d[n-1][m-1])
    
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    solution(n, m,arr)