# 백준 / 단계별로 풀어보기 / 15. 약수, 배수와 소수 2 / 1934번 최소공배수
import sys

def find_GCD(x: int, y: int):
    common_divisor = []
    length = max(x, y) // 2
    
    for i in range(1, length + 1):
        if x % i == 0 and y % i == 0:
            common_divisor.append(i)
    
    return max(common_divisor)

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == m : 
        print(n)
        continue
    
    gcd = find_GCD(n, m)
    print(int((n * m) / gcd))
