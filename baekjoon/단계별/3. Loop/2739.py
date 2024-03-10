import sys

def solution():
    n = int(sys.stdin.readline())

    for i in range(1, 10):
        print(f'{n} * {i} = {n*i}')

def main():
    solution()

if __name__ == "__main__":
    main()