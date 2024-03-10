import sys
from math import ceil

def solution():
    n = int(sys.stdin.readline().rstrip())
    devided = []
    if n == 1: return
    i = 2

    while True:
        if n == 0 or i > n: break
        if n % i == 0:
            n //= i
            devided.append(i)
            continue
        i += 1

    for j in devided:
        print(j)

if __name__ == '__main__':
    solution()