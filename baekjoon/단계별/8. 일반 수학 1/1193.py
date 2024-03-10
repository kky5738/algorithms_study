# 백준 1193번 분수찾기

import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    k = 0
    
    for i in range(round(n**0.5)+1):
        d1 = i*2 + 1
        d2 = 4 if i % 2 == 0 else 2
        k += 1 if i % 2 == 0 else int(d2*i)            
        num = k

        for j in range(int(n/2)):
            add = 0
            if i % 2 == 0:
                if j % 2 == 0:
                    add = int(d2*(j/2))
                else:
                    add = d1
            elif i % 2 != 0:
                if j % 2 == 0 and j != 0: 
                    add = d1
                elif j % 2 != 0:
                    add = int(d2*j)
            num += add
            if num == n: return print(f'{i+1}/{j+1}')

if __name__ == '__main__':
    solution()