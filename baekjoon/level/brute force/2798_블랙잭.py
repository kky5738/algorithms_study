# 백준 2798번 블랙잭
import sys
from itertools import combinations

def main():
    solution()

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    cards = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    combi = list(combinations(cards, 3))
    result = sum(combi[0])
    min_dist = abs(sum(combi[0]) - m)
    
    for (x, y, z) in combi:
        condition = abs(x + y + z - m)
        if condition == 0:
            result = x + y + z
            return print(result)
        elif condition < min_dist:
                min_dist = condition
                result = x + y + z
                
    print(result)

if __name__ == '__main__':
    main()