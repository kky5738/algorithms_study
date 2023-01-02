import sys

def solution():
    # 다이얼-문자, 다이얼-시간
    inputs = sys.stdin.readline().rstrip()
    
    time = [i+1 for i in range(2, 10, 1)]
    print(time)
    pass

if __name__ == '__main__':
     solution()