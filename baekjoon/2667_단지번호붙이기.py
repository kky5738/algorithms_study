# 백준 DFS BFS 추천문제집 2668번 단지번호붙이기
from collections import deque

def bfs(x, y, g, n):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    queue = deque()
    queue.append((x, y))
    
    while queue and g[x][y]:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if g[nx][ny] == 0:
                continue
            if g[nx][ny] == 1:
                queue.append((nx, ny))
                cnt += 1
                g[nx][ny] = g[x][y] + 1
                
    if not cnt and g[x][y] == 1:
        cnt = 1
    return cnt
    
def solution(graph, n):
    res = []
    for i in range(n):
        for j in range(n):
            cnt = bfs(i, j, graph, n)
            if cnt:
                res.append(cnt)
    
    return res

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    
    res = solution(graph, n)
    
    print(len(res))
    res.sort()
    for x in res:
        print(x)
    
    for i in range(n):
        print(graph[i])