# 백준 DFS BFS 추천문제집_2331번 반복수열
def solution(a, p):

    arr = [a]
    def bfs(a, p, arr: list):
        from collections import deque
        
        queue = deque()
        queue.append((a))
        while queue:
            a = queue.popleft()
            num = 0
            for x in str(a):
                num += int(x)**p
            
            if num not in arr:
                arr.append(num)
                queue.append(num)
            else:
                return arr[:arr.index(num)]
                
            
    arr = bfs(a, p, arr)
    
    return len(arr)

if __name__ == "__main__":
    A, P = map(int, input().split())
    
    res = solution(A, P)
    print(res)