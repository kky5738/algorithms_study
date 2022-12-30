import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    inputs = sys.stdin.readline().rstrip()
    answer = 0

    for num in inputs:
        answer += int(num)

    print(answer)

if __name__ == '__main__':
    solution()