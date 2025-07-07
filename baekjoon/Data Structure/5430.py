import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input() # 함수 리스트
    n = int(input()) # 배열 길이
    arr = input() # [a1, a2, ..., an] 형태의 정수 배열
    arr = deque(arr.strip("[]").split(","))
    
    r = False
    try:
        for func in p:

            if func == "R":
                r = not r
                
            elif func == "D":
                if not arr or n == 0:
                    raise IndexError
                if r: # 뒤집어졌다면
                    arr.pop()
                else:
                    arr.popleft()
            
        if r:
            print(f"[{','.join(list(arr)[::-1])}]")
        else:
            print(f"[{','.join(arr)}]")
    except IndexError:
        print("error")