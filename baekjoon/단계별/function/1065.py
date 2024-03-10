import sys

def get_num(n):
    n = list(map(int, str(n)))
    return n[0] - n[1] == n[1] - n[2]
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    
    if n < 100:
        return print(n)

    result = 99

    for i in range(101, n):
        result += get_num(i+1)

    print(result)

if __name__ == '__main__':
    solution()