import sys

def solution():
    input = sys.stdin.readline

    while True:
        try:
            a, b = map(int, input().split(' '))
        except ValueError:
            break

        print(a+b)

def main():
    solution()

if __name__ == '__main__':
    main()