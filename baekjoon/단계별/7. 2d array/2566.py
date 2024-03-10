import sys

def solution():
    maxi = [] # (col, value)
    columns = []

    for _ in range(9):
        temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

        max_n = max(temp)
        maxi.append(max_n)

        col = temp.index(max_n)
        columns.append(col)

    print(max(maxi))
    print(maxi.index(max(maxi))+1, columns[maxi.index(max(maxi))]+1)

if __name__ == '__main__':
    solution()