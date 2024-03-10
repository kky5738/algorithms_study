import sys

def solution():
    c = int(sys.stdin.readline().rstrip())

    for _ in range(c):
        array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        len = array.pop(0)
        avg = sum(array)/len
        cnt = 0
        
        for score in array:
            cnt += 1 if score > avg else 0        
        
        print(f'{round(cnt/len*100, 3):.3f}%')

if __name__ == '__main__':
    solution()