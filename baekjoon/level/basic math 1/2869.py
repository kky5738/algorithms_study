import sys

def get_a_n(a_1, n, d):
    return a_1 + ((n - 1) * d)

def solution():
    a, b, v = map(int, sys.stdin.readline().rstrip().split(' '))
    answer = 1
    if a == v: return print(1)
    d = a - b
    n = v // d
    a_n = get_a_n(0, n, d)
    
    print('n:', n, ', a_n:', a_n)
    # 크면 n - b
    # v - a_n > a -> n + 2
    # n + 1
    
    if a_n < v:
        pass
    
    elif a_n == v:
        
        pass


    print(answer)

if __name__ == '__main__':
    solution()