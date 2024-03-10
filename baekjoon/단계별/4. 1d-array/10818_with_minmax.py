import sys

def solution():
    input = sys.stdin.readline
    n = int(input().rstrip())
    array = list(map(int, input().rstrip().split()))
    
    print(min(array), max(array))

if __name__ == '__main__':
    solution()