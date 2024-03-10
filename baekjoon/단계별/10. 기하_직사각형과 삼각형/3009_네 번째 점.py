# 백준 3009번 네 번째 점
import sys
from collections import Counter

def solution():
    x, y = [], []
    for _ in range(3):
        point1, point2 = map(int, sys.stdin.readline().rstrip().split())
        x.append(point1)
        y.append(point2)
    
    x_cnt, y_cnt = Counter(x), Counter(y)
    result = (x_cnt.most_common()[-1][0], y_cnt.most_common()[-1][0])
    
    print(result[0], result[1])
    
if __name__ == '__main__':
    solution()