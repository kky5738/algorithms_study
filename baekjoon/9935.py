# BOJ 9935 문자열 폭발

import sys

def solution():
    s = list(sys.stdin.readline().rstrip())
    bomb = sys.stdin.readline().rstrip()
    len_bomb = len(bomb)
    answer = []
    
    for x in s:
        answer.append(x)
        if x == bomb[-1]:
            if bomb == ''.join(answer[-len_bomb:]):
                for _ in range(len_bomb):
                    answer.pop()
    
    print(''.join(answer) if answer else 'FRULA')
    

if __name__ == "__main__":
    solution()