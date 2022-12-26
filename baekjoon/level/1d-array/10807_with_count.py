import sys

def solution():
    input = sys.stdin.readline
    int(input().rstrip())
    array = list(map(int, input().rstrip().split(' ')))
    v = int(input().rstrip())
    
    print(array.count(v))

if __name__ == '__main__':
    solution()