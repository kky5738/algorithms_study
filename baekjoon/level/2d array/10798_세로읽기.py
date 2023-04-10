# 백준 10798번 세로읽기

import sys

def solution():
    text = []
    max_len = 0
    for _ in range(5):
        input_str = sys.stdin.readline().rstrip()
        text.append(input_str)
        if len(input_str) > max_len: max_len = len(input_str)

    for string in text:
        if len(string) < max_len:
            pad = max_len - len(string)
            text[text.index(string)] += ' '*pad
            
    result = ''
    idx = 0
    while idx < max_len:
        for i in range(5):
            result += text[i][idx]
        idx += 1
        
    print(result.replace(' ', ''))
if __name__ == '__main__':
    solution()