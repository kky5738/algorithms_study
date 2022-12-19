import sys

def solution():
    input = sys.stdin.readline
    n = int(input())

    for i in range(n):
        print('*'*(i+1))

def main():
    solution()

if __name__ == '__main__':
    main()