def solution():
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    # dfs and bfs
    result_dfs = []
    result_bfs = []
    
    def dfs(graph, v, visited):
        visited[v] = True
        result_dfs.append(v)
        for i in sorted(graph[v]):
            if not visited[i]:
                dfs(graph, i, visited)

    def bfs(graph, started):
        from collections import deque
        queue = deque([started])
        visited = [False] * (n+1)
        visited[started] = True
        while queue:
            v = queue.popleft()
            result_bfs.append(v)
            for i in sorted(graph[v]):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
    visited = [False] * (n+1)
    dfs(graph, start, visited)
    bfs(graph, start)
    
    for x in result_dfs:
        print(x, end=' ')
    print()
    for x in result_bfs:
        print(x, end=' ')
            
if __name__ == "__main__":
    solution()