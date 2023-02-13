# 백준 2447번 별 찍기 - 10
import sys

def main():
    solution()

def solution():
    n = int(sys.stdin.readline().rstrip())
    # for i in range(n):
        # print(f'{i}//3 = {i//3},  {i} % 3 = {i % 3}, {i} / 3 = {i / 3}')
    
    print_star(n*n)

def print_star(n):
    if n < 0: return
    if n-1 % 3 == 1:
        print()
        
    print('*', end='')
    return print_star(n-1)

    
# 00 01 02 10 11
if __name__ == '__main__':
    main()