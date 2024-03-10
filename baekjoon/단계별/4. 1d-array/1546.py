import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    score = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    m = max(score)
    answer = 0

    for i in score:
        answer += i/m*100/n
        
    print(answer)
    
if __name__ == '__main__':
    solution()