# 백준_단계별로 풀어보기_12.BruteForce_1018번 체스판 다시 칠하기
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

w = 'WBWBWBWB'
b = 'BWBWBWBW'

boad = []

for _ in range(n):
    boad.append(sys.stdin.readline().rstrip())

def check_boad(n, m, boad, pattern1, pattern2):
    result = []
    for r in range(n-8+1):
        for c in range(m-8+1):
            diff = 0
            for i in range(r, r+8):
                for j in range(c, c+8):
                    if i % 2 == 0:
                        # print(int(boad[i][j] != pattern1[j]), end='')
                        diff += int(boad[i][j] != pattern1[j-c])
                    else:
                        # print(int(boad[i][j] != pattern2[j]), end='')
                        diff += int(boad[i][j] != pattern2[j-c])
                # print()
                    
            result.append(diff)
    return result

white = check_boad(n, m, boad, w, b)
black = check_boad(n, m, boad, b, w)

white_min = min(white)
black_min = min(black)

print(min(white_min, black_min))