# 백준 문제집 DFS, BFS 추천문제_2178 미로탐색

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    from collections import deque
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            cur_x, cur_y = x + dx, y + dy
            if not(0 <= cur_x < n) or not(0 <= cur_y < m):
                continue
            if graph[cur_x][cur_y] == 0:
                continue
            if graph[cur_x][cur_y] == 1:
                queue.append((cur_x, cur_y))
                graph[cur_x][cur_y] = graph[x][y] + 1
                
bfs(0, 0)
print(graph[n-1][m-1])