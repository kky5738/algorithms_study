import sys
from collections import Counter

def solution():
    string = sys.stdin.readline().rstrip()
    c = Counter(string.upper())

    most = c.most_common()

    if len(most) == 1:
        print(most[0][0])
        return

    if most[0][1] != most[1][1]:
        print(most[0][0])
    else:
        print('?')

if __name__ == '__main__':
    solution()