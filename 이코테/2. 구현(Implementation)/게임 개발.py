import sys

MAX = 2000

def solution(n, m, a, b, d, grid):
    direction = [0, 1, 2, 3]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    """
    1. move[d - 1]
    2. if not move[d-1]:
    """
    answer = 1
    idx = 0
    while idx < MAX:
        
        for _ in range(4):
            d = direction[d-1]
            x, y = move[d]
            if not grid[a + x][b + y]:
                grid[a + x][b + y] = 1
                grid[a][b] = 1
                a += x
                b += y
                answer += 1
                break
        else:
            x, y = move[d]
            if grid[a - x][b - y]:
                break
            a -= x
            b -= y
        idx += 1
        
    return answer

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a, b, d = map(int, sys.stdin.readline().rstrip().split())
    grid = []
    
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

    cnt = solution(n, m, a, b, d, grid)
    print(cnt)