# 백준 2231번 분해합
import sys

def main():
    solution()
    
def solution():
    n = sys.stdin.readline().rstrip()
    result = []
    for x in range(int(n), int(n) - 10*len(n), -1):
        if x < 1: break
        generator = x
        array_x = str(x)
        
        for i in array_x:
            generator += int(i)

        if generator == int(n):
            result.append(x)
            
    if not result:
        return print(0)
    
    result.sort()
    print(result[0])
    
if __name__ == "__main__":
    main()