# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# # 지역의 최소 및 최대 높이 찾기
# min_height = min(map(min, graph))
# max_height = max(map(max, graph))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y, limit, visited):
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = 1  # BFS 시작 시 방문 처리

#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
            
#             if 0 <= nx < n and 0 <= ny < n:  # 범위 체크
#                 if graph[nx][ny] > limit and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     queue.append((nx, ny))

# # 물에 잠기지 않는 최대 안전 영역 개수 저장
# max_safe_area = 1  # 아무 지역도 물에 잠기지 않을 수도 있음

# for water_level in range(min_height, max_height + 1):
#     visited = [[0] * n for _ in range(n)]
#     safe_area_count = 0

#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] > water_level and visited[i][j] == 0:
#                 bfs(i, j, water_level, visited)
#                 safe_area_count += 1
    
#     max_safe_area = max(max_safe_area, safe_area_count)

# print(max_safe_area)

# 아래는 GPT와 함께 안전 영역 문제를 작은 문제들로 쪼개 단계별로 문제를 해결해보고 완성된 안전영역 풀이
import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def bfs(x, y, visited, graph, h):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))

height = max(map(max, arr))  # 가장 높은 지점 찾기
answer = 1  # 최소 안전 영역 개수 (비가 전혀 안 올 경우)

for h in range(height):
    visited = [[False] * n for _ in range(n)]  # 💡 높이가 바뀔 때마다 visited 초기화
    safe = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                bfs(i, j, visited, arr, h)
                safe += 1  # 새로운 안전 영역 발견

    answer = max(safe, answer)  # 최대 개수 갱신
    
print(answer)