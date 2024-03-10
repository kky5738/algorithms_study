import sys

def solution():
    answer = [i+1 for i in range(30)]
    
    for _ in range(28):
        x = int(sys.stdin.readline().rstrip())
        answer.remove(x)

    sorted(answer)
    print(answer[0])
    print(answer[1])

if __name__ == '__main__':
    solution()