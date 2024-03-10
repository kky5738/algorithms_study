# 백준 2587번 대표값2
import sys

def main():
    solution()
    
def solution():
    
    array = []
    array.append(int(sys.stdin.readline().rstrip()))
    
    for i in range(4):
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
                
    sum = 0
    for i in array:
        sum += i
    avg = int(sum/5)
    mid = array[2]
    
    print(avg)
    print(mid)
    
if __name__ == '__main__':
    main()