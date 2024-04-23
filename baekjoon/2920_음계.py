import sys

def solution(major):
    a = '1 2 3 4 5 6 7 8'
    d = '8 7 6 5 4 3 2 1'
    if major == a:
        print('ascending')
    elif major == d:
        print('descending')
    else:
        print('mixed')
        
if __name__ == "__main__":
    major = sys.stdin.readline().rstrip()
    solution(major)
