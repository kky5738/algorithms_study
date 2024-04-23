import sys
from itertools import combinations

def solution(n, k):
    n = [i for i in range(n)]
    comb = list(combinations(n, k))
    return len(comb)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rstrip().split())
    result = solution(n, k)
    print(result)