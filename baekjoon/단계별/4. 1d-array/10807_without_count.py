import sys

def solution():
    input = sys.stdin.readline
    n = int(input().rstrip())
    array = list(map(int, input().rstrip().split(' ')))
    target = int(input().rstrip())
    count = 0
    
    for i in range(n):
        if array[i] == target:
            count += 1
    
    print(count)

if __name__ == '__main__':
    solution()