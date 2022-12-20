import sys

def solution():
    input = sys.stdin.readline

    while True:
        a, b = map(int, input().split(' '))
        # if a == '^Z':
        #     break
        print(a+b)

def main():
    solution()

if __name__ == '__main__':
    main()