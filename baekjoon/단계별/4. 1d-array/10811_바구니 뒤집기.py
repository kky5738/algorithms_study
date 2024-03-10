import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

result = [i+1 for i in range(n)]

for j in range(m):
    # start, end
    s, e = map(int, sys.stdin.readline().rstrip().split())
    
    left = result[:s-1]
    reverse = list(reversed(result[s-1:e]))
    right = result[e:]
    
    result = left + reverse + right

for x in result:
    print(x, end=' ')