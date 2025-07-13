import sys
from collections import deque
input = lambda : sys.stdin.readline()

n, k = map(int, input().split())

q = deque([str(i) for i in range(1, n+1)])

index = 0
result = []
while q:
    temp = q.popleft()
    index += 1
    
    if index % k == 0:
        result.append(temp)
    else:
        q.append(temp)

print(f"<{', '.join(result)}>")