# 백준 2798번 블랙잭
import sys
from itertools import combinations

def main():
    solution()

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    cards = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    combi = list(combinations(cards, 3))
    result = 0
    plus = sum(combi[0])
    min_dist = abs(m - sum(combi[0]))

    for (x, y, z) in combi:
        plus = x + y + z
        
        if plus == m: return print(plus)
        
        elif plus < m and abs(m - plus) < min_dist:
            min_dist = abs(m - plus)
            result = plus

    print(result)

if __name__ == '__main__':
    main()