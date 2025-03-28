def practice_5_10():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1

    print(result)
    
def practice_5_11():
    # bfs 쓰기
    from collections import deque
    
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
            
    bfs(0, 0)
    result = graph[n-1][m-1]
    print(graph)
    print(result)

if __name__ == "__main__":
    # practice_5_10()
    practice_5_11()