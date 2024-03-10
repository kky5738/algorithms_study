import sys
import re

def solution():
    string = sys.stdin.readline().rstrip()
    
    p = re.compile('[a-zA-Z]+')
    print(len(p.findall(string)))

if __name__ == '__main__':
    solution()