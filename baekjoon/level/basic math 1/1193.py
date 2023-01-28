# 백준 1193번 분수찾기
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    for i in range(int(n**0.5), n+1):
        s = (i*i + i)/2   # n(n+1) / 2
        if s >= n:
            level = i        
            break
    start_idx = int(((level - 1) * (1+(level-1))) / 2) + 1

    if level % 2 == 0:
        x = 1
        y = level
        for _ in range(start_idx, n):
            x += 1
            y -= 1
        answer = f'{x}/{y}'

    else:
        x = level
        y = 1
        for _ in range(start_idx, n):
            x -= 1
            y += 1
        answer = f'{x}/{y}'

    print(answer)

if __name__ == '__main__':
    solution()