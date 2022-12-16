import sys

def solution():
    n = int(sys.stdin.readline())
    nums = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

    for i in range(n):
        print(sum(nums[i]))

def main():
    solution()

if __name__ == '__main__':
    main()