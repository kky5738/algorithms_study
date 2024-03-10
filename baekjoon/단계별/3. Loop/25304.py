import sys

def solution():
    x = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    results = 0

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split(' '))
        results += a*b
    
    print('Yes' if results == x else 'No')

def main(): 
    solution()

if __name__ == "__main__":
    main()