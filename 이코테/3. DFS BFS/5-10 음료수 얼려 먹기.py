import sys

def solution(graph, n, m):
    
    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        if graph[x][y] == 0:
            print(x+1, y+1)
            graph[x][y] = 1

            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    return result
  

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    res = solution(arr, n, m)
    
    print(res)