# BOJ 1325 효율적인 해킹.
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(100_000)

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    count = 1

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1
    return count

def solution(n, m, graph):
    result = []
    max_count = 0
    counts = [0] * (n + 1)

    for i in range(1, n + 1):
        counts[i] = bfs(i, graph, n)
        if counts[i] > max_count:
            max_count = counts[i]

    for i in range(1, n + 1):
        if counts[i] == max_count:
            result.append(i)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)  # b를 해킹하면 a도 해킹 가능

    solution(n, m, graph)
