import sys

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for num in range(t):
        answer = []
        
        n = int(sys.stdin.readline().rstrip())
        for idx, coin in zip(range(4), [25, 10, 5, 1]):
            answer.append(n // coin)
            n = n % coin
        
        for i in range(4):
            print(answer[i], end=' ')
        print()

if __name__ == '__main__':
    solution()