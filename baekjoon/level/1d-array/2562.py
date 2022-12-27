import sys

def solution():
    max = idx = 0

    for i in range(9):
        n = int(sys.stdin.readline().rstrip())
        if n > max:
            max = n
            idx = i

    print(max)
    print(idx+1)


if __name__ == '__main__':
    solution()