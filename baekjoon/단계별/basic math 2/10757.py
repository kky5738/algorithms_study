# 백준 10757번 큰 수 A+B
import sys

def main():
    solution()

def solution():
    a, b = map(list, sys.stdin.readline().rstrip().split(' '))
    a.reverse()
    b.reverse()

    if len(a) != len(b):
        bigger = a if len(a) > len(b) else b
        smaller = a if len(a) < len(b) else b
        
        padding = ['0' for _ in range(len(bigger) - len(smaller))]
        smaller += padding
        a = bigger
        b = smaller

    answer = ''
    length = len(a)
    carry = 0

    for i in range(length):
        x = int(a[i]) + int(b[i]) + carry
        if x >= 10:
            answer += str(x)[1]
            carry = 1
        else:
            answer += str(x)
            carry = 0
    if carry == 1:
        answer += '1'

    print(answer[::-1])

if __name__ == '__main__':
    main()