import sys

def solution():
    answer = []

    for _ in range(10):
        x = int(sys.stdin.readline().rstrip())
        answer.append(x % 42)

    answer = set(answer)
    print(len(answer))

if __name__ == '__main__':
    solution()