# 백준 DFS BFS 추천 문제_10451 순열 사이클
import sys
sys.setrecursionlimit((10**3) + 5)
def solution(graph, n):
    visited = [True, True] + [False] * (n - 1)
    
    def dfs(graph, v, visited):
        visited[v] = True
        if v == graph[v-1]:
            return True
        if not visited[graph[v-1]]:
            dfs(graph, graph[v-1], visited)
            return True
        return False
    
    cnt = 0
    for i in range(1, n+1):
        if dfs(graph, i, visited) == True:
            cnt += 1
    return cnt

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = list(map(int, input().split()))
        res = solution(graph, n)
        print(res)