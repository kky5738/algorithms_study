# 백준 2563번 색종이
# 두 영역만 겹치는 경우는 맞지만 그 이상 겹치는 경우까지 고려해야 함
import sys
from itertools import combinations

def main():
    solution()

def solution():
    n = int(sys.stdin.readline().rstrip())
    loc = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        loc.append([x, y])
        
    comb = list(combinations(loc, 2))
    width = 0

    for d1, d2 in comb:
        x1, y1 = d1
        x2, y2 = d2
        
        x_d = abs(x1 - x2)
        y_d = abs(y1 - y2)

        if x_d + y_d >= 10:
            continue
        else:
            width += (10 - x_d) * (10 - y_d)
    
    print(n * 100 - width)

if __name__ == '__main__':
    main()