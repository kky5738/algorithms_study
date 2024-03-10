# 백준 25305번 커트라인
import sys

def main():
    solution()
    
def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split(' '))
    
    array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    print(array[-k])

if __name__ == '__main__':
    main()