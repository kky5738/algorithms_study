import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        answer = sys.stdin.readline().rstrip()
        count = 0
        score = 0

        for c in answer:
            count = 0 if c != 'O' else count + 1
            score += count
        
        print(score)

if __name__ == '__main__':
    solution()