# 백준 25501번 재귀의 귀재
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    
    for _ in range(n):
        flag, count = isPalindrome(sys.stdin.readline().rstrip())
        print(flag, count)

def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt)
    
def isPalindrome(s:str):
    return recursion(s, 0, len(s)-1, 0)

if __name__ == '__main__':
    main()