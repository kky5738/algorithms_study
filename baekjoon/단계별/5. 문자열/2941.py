import sys
import re

def solution():
    inputs = sys.stdin.readline().rstrip()
    answer = inputs
    croatia = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
    
    for c in croatia:
        if c in inputs:
            answer = re.sub(c, 'a', answer)

    print(len(answer))

if __name__ == '__main__':
    solution()