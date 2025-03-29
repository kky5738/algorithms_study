# BOJ 1012 유기농 배추
import sys
from collections import deque

def bfs(x:int, y:int, visited: list[list[bool]], graph: list[list[int]]):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    

def solution(m:int, n:int, graph:list[list[int]]):
    visited = [[False] * m for _ in range(n)]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j, visited, graph)
                answer += 1
    
    print(answer)

if __name__ == "__main__":
    input = sys.stdin.readline
    
    t = int(input().rstrip())
    for _ in range(t):
        m, n, k = map(int, input().rstrip().split())
        ground = [[0] * m for _ in range(n)]
        
        for _ in range(k):
            x, y = map(int, input().rstrip().split())
            ground[y][x] = 1
        
        solution(m, n, graph=ground)