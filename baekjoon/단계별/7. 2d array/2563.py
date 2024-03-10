# 백준 2563번 색종이
import sys

def main():
    solution()

def make_square(square:list, x: int, y: int, l: int) -> list:

    y_idx = l - y - 10
    
    for i in range(10):
        for j in range(10):
            square[y_idx+i][x+j] += 1

    return square

def solution():

    n = int(sys.stdin.readline().rstrip())
    l = 100
    square = [[0 for _ in range(l)] for _ in range(l)]
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        square = make_square(square, x, y, l)
    
    answer = 0

    for i in range(l):
        for j in range(l):
            if square[i][j] > 0: answer += 1
   
    print(answer)

if __name__ == '__main__':
    main()