import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    answer = 0

    for _ in range(n):
        inputs = sys.stdin.readline().rstrip()
        answer += check(inputs)
    
    print(answer)

def check(string:str) -> int:
    checker = []

    for idx, c in enumerate(string):
        if not c in checker:
            checker.append(c)
            
        else:
            if idx - checker.index(c) > 1 and checker[-1] != c:
                return 0

    return 1

if __name__ == '__main__':
    solution()