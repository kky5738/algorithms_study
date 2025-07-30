import sys
from collections import deque

input = lambda : sys.stdin.readline()

n = int(input())
cards = deque([i for i in range(1, n+1)])
cnt = 0
while cards and (n - (cnt // 2)) != 1:
    cards.popleft()
    cards.append(cards.popleft())
    cnt += 2
    
print(cards[0])