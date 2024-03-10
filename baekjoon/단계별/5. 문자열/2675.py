import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        mul, inputs = sys.stdin.readline().rstrip().split(' ')
        
        for c in inputs:
            print(c*int(mul), end='')
        print()

if __name__ == '__main__':
    solution()