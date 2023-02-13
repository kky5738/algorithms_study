# 백준 2447번 별 찍기 - 10
import sys

def main():
    solution()

def solution():
    global n_pow
    
    n = int(sys.stdin.readline().rstrip())
    n_pow = n*n
    # for i in range(n):
        # print(f'{i}//3 = {i//3},  {i} % 3 = {i % 3}, {i} / 3 = {i / 3}')
    
    print_star(n_pow)

def print_star(n):
    global n_pow
    if n == 0: return
    if n % n_pow**0.5 == 0 and n != n_pow:
        print()
    # if n < n_pow // 3
    print('*', end='')
    return print_star(n-1)

    
# 00 01 02 10 11
if __name__ == '__main__':
    main()
    