# 다른 탐색 알고리즘도 써보기
import sys

def solution():
    input = sys.stdin.readline
    n = int(input().rstrip())
    array = list(map(int, input().rstrip().split()))
    min = max = array[0]

    for num in array:
        if num > max: max = num
        if num < min: min = num

    print(min, max)

if __name__ == '__main__':
    solution()