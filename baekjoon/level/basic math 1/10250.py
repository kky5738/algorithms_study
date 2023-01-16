import sys
from math import ceil

def solution():
    test_case = int(sys.stdin.readline().rstrip())
    for i in range(test_case):
        h, w, n = map(int, sys.stdin.readline().rstrip().split(' '))
        answer = f'{int(n%h) if n%h != 0 else h}' + f'{ceil(n/h)}'.zfill(2)
        print(answer)

if __name__ == '__main__':
    solution()