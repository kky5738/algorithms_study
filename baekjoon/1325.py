# BOJ 1325 효율적인 해킹
import sys
from collections import deque, defaultdict

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        v = q.popleft()
        for node in graph[v]:
            if not visited[node]:
                cnt += 1
                q.append(node)
                visited[node] = True
    
    return [cnt, start]

def solution(n: int, m: int, graph: list[list[int]]): # 방향 설정이 잘못된 코드
    answer = [[] for _ in range(n + 1)]
    maxi = 0
    for i in range(n):
        if graph[i]:
            visited = [False] * (n + 1)
            cnt, com = bfs(i, graph, visited)
            answer[cnt].append(com)
            maxi = max(maxi, cnt)

    print(' '.join(map(str, sorted(answer[maxi]))))

def solution_from_gpt(n: int, m: int, graph: list[list[int]]): # 근데 이것도 시간 초과 발생ㅇ함... 다시 해보자
    max_hack = 0
    result = []
    
    def dfs(v):
        visited[v] = True
        cnt = 1
        for node in graph[v]:
            if not visited[node]:
                cnt += dfs(node)
        return cnt
    
    for i in range(1, n+1):
        visited = [False] * (n+1)
        count = dfs(i)
        
        if count > max_hack:
            max_hack = count
            result = [i]
        elif count == max_hack:
            result.append(i)
    
    print(" ".join(map(str, sorted(result))))

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n, m = map(int, input().rstrip().split())
    # graph = [list() for _ in range(n+1)]
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        graph[b].append(a)
    
    # solution(n, m, graph)
    solution_from_gpt(n, m, graph)