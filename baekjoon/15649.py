# BOJ 15649 N과 M (1)
import sys

def dfs(n, m, path, used):
    # 길이가 M이면 출력하고 종료
    if len(path) == m:
        print(" ".join(map(str, path)))
        return

    for i in range(1, n + 1):
        if not used[i]:  # 중복 방지
            used[i] = True  # 선택한 숫자는 사용 처리
            dfs(n, m, path + [i], used)  # 재귀 호출
            used[i] = False  # 백트래킹: 원상복구

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    used = [False] * (n + 1)  # 사용 여부 체크 배열
    dfs(n, m, [], used)

if __name__ == "__main__":
    solution()