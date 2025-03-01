# 백준 1966 프린터 큐

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    prio = list(map(int, sys.stdin.readline().rstrip().split()))    
    q = deque([(i, v) for i, v in enumerate(prio)])
    ans = 0
    maximum = max(prio)
    
    while q:
        i, v = q.popleft()
        
        if v == maximum:
            ans += 1
            prio.remove(v)
            
            if i == m:
                print(ans)
                break
            
            maximum = max(prio)    
            continue
        else:
            q.append((i, v))