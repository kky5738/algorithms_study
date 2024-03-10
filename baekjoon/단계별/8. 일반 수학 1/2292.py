import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    x = 1

    for i in range(n):
        a = x + 6 * i
        if n - a <= 0:
            return print(i + 1)
        x = a

if __name__ == '__main__':
    solution()