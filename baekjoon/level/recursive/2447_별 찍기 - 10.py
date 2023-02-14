# 백준 2447번 별 찍기 - 10
import sys
from math import ceil

def main():
    solution()

def solution():
    global n_pow
    
    n = int(sys.stdin.readline().rstrip())
    n_pow = n*n
    # for i in range(n):
        # print(f'{i}//3 = {i//3},  {i} % 3 = {i % 3}, {i} / 3 = {i / 3}')
    
    print_star(n)

def print_star(n):
    global n_pow
    if n == 0: return
    
    for i in range(int(n_pow**0.5)):
        if n % 3 == 2 and i % 3 == 1:
            print(' ', end='')
            continue
        
        print('*', end='')
    if n != 1:
        print()
    return print_star(n-1)


    
# 00 01 02 10 11
if __name__ == '__main__':
    main()
    
    """
    4~6
    n/3
    n < n // 3 or n > (n // 3) * 2
    10~18
    """