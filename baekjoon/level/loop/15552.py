import sys

def solution():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split(' '))
        print(a+b)

def main():
    solution()

if __name__ == '__main__':
    main()