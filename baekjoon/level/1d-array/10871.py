import sys

def solution():
    input = sys.stdin.readline
    n, x = map(int, input().rstrip().split(' '))
    array = list(map(int, input().rstrip().split()))
    result = []
    
    for num in array:
        if num < x:
            result.append(num)
            print(num, end=' ')

if __name__ == '__main__':
    solution()