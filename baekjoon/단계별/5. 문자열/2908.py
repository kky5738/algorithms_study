import sys

def solution():
    a,b = sys.stdin.readline().rstrip().split(' ')
    max = a if a[::-1] > b[::-1] else b
    
    print(max[::-1])

if __name__ == '__main__':
    solution()