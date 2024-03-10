# 백준 2750번 수 정렬하기
import sys

def main():
    solution()

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    array = []
    array.append(int(sys.stdin.readline().rstrip()))
    
    for i in range(n-1):
        x = int(sys.stdin.readline().rstrip())
        
        for idx, j in enumerate(array):
            if x < j:
                array.insert(idx, x)
                break
            elif x >= j:
                if idx + 1 == len(array):
                    array.append(x)
                    break
                else: continue
                    
    for i in range(n):
        print(array[i])
    
if __name__ == '__main__':
    main()