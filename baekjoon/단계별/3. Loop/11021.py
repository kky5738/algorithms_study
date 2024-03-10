import sys

def solution():
    input = sys.stdin.readline
    t = int(input())

    for i in range(t):
        a, b = map(int, input().split(' '))
        print(f'Case #{i+1}: {a+b}')

def main():
    solution()

if __name__ == '__main__':
    main()