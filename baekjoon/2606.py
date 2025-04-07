# BOJ 2606 바이러스
# 1번 노드와 연결된 컴퓨터 개수 구하기. n <= 100 이므로 O(n^2) 이하로 구성하기
# 처음엔 단방향 그래프로 구현하여 틀림. 이후 질문 게시판에서 양방향 그래프임을 확인하고 통과

import sys
from collections import defaultdict, deque

def bfs(start, graph, visited):
    q = deque([start])
    infected = 0 # 1번 컴퓨터 포함일 경우 cnt는 1 아니라면 0
    visited[start] = True
    
    # 기본적인 BFS. 시작 노드 방문 처리 후 이어지는 노드가 있을 경우 큐에 모두 삽입 후 하나씩 꺼내서 탐색.
    while q:
        v = q.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                infected += 1 # 1번과 연결된 컴퓨터 수 +1
    
    return infected

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n = int(input().rstrip())
    connections = int(input().rstrip())
    network = defaultdict(list)
    
    for _ in range(connections):
        a, b = map(int, input().rstrip().split())
        
        # 양방향 그래프
        network[a].append(b)
        network[b].append(a)
    
    visited = [False] * (n + 1)
    
    # defaultdict는 hash를 이용하기 때문에 1을 index로 처리하지 않고 key로 처리 함.
    # 따라서 1을 BFS 시작점으로 주어도 1에 해당하는 key의 value인 1번 컴퓨터와 연결된 리스트를 탐색하므로
    # 주어진 순서에 상관없이 1번 컴퓨터부터 탐색 가능
    print(bfs(1, network, visited))