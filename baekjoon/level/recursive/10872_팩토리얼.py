# 백준 10872번 팩토리얼
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    
    fact_n = factorial(n)
    print(fact_n)
    
def factorial(n: int):
    if n == 0: return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    main()