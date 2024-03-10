import sys

def solution():
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    try:
        break_even_point = int(a / (c - b)) + 1
    except:
        print(-1)
    else:
        print(break_even_point if break_even_point > 0 else -1)

if __name__ == '__main__':
    solution()