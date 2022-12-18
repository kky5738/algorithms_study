import sys

def recur(num: int) -> int:
    if num < 1: return 0
    return num + recur(num-1)
    
def solution():
    n = int(sys.stdin.readline())
    print(recur(n))

def main():
    solution()

if __name__ == '__main__':
    main()