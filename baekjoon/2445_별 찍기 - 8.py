# 백준 2445번 별 찍기 - 8
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    for i in range((2*n)-1):
        for j in range(2*n):
            
            print('*', end='')
        print()
if __name__ == "__main__":
    main()