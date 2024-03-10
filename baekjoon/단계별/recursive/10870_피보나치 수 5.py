# 백준 10870번 피보나치 수 5
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    
    answer = fibo(n)
    print(answer)

def fibo(n: int):
    if n == 0: return 0
    if n == 1: return 1
    
    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    main()