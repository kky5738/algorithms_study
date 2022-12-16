import sys
from collections import Counter

def mode_a(data:list):
    common_num = Counter(data).most_common() 
    result = 0

    if len(common_num) > 1:
        if common_num[0][1] == common_num[1][1]:
            result = common_num[1][0]
        else:
            result = common_num[0][0]
    else:
        result = common_num[0][0]

    return result

def solution():
    n = int(sys.stdin.readline())
    li = [0 for _ in range(n)]

    for i in range(n):
        li[i] = int(sys.stdin.readline())

    li.sort()

    print(round(sum(li) / n))
    print(li[n // 2])
    print(mode_a(li))
    print(li[-1] - li[0])

def main():
    solution()

if __name__ == '__main__':
    main()