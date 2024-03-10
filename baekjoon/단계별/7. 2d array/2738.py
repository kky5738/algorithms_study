import sys

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    a = []
    b = []
    result = []

    for _ in range(n):
        matrix = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        a.append(matrix)

    for _ in range(n):
        mat = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        b.append(mat)

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(a[i][j] + b[i][j])
        result.append(temp)

    for i in range(n):
        for j in range(m):
            print(f'{result[i][j]}', end=' ')
        print()

if __name__ == '__main__':
    solution()