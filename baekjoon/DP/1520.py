# BOJ 1520 내리막길
# dfs + dp 문제인 줄 몰라서 gpt 도움 받음. 나는 DP로만 해결 시도했고 틀림
import sys

sys.setrecursionlimit(10**6)

def dfs(x: int, y: int, n: int, m: int, graph: list[list[int]], dp: list[list[int]]):
    """
    Args:
        x (int): x좌표
        y (int): y좌표
        n (int): raw
        m (int): column
        graph (list[list[int]]): 탐색하려는 2차원 리스트
        dp (list[list[int]]): 메모이제이션을 위한 dp 테이블
    """
    # 종료 조건: 도착 지점이면 경로 1개 추가
    if x == n - 1 and y == m - 1:
        return 1
    
    # 이미 방문했으면 저장된 dp 테이블 값 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문 설정
    dp[x][y] = 0
    
    # 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # 그래프 범위 체크, 내리막길 조건 체크
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny, n, m, graph, dp)
    
    return dp[x][y]

def solution(n: int, m: int, graph: list[list[int]]) -> None:
    # -1로 초기화하여 방문 여부 체크
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    
    print(dfs(0, 0, n, m, graph, dp))

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    solution(n, m, graph)
