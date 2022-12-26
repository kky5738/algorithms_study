# 1 빼고는 다 가능
import sys 

def solution():
    n = sys.stdin.readline().rstrip()
    if int(n) == 0: return print(1)
    s = n
    count = 0
    if int(s) < 10: s = '0' + s[-1]
    print(s)
    
    while True:
        if s == n and count != 0: break
        
        m = str(int(s[0]) + int(s[1])) # 1
        s = s[-1] + m[-1]
        print(s)
        count += 1
        # if count == 10: return
        
    print(count)
def main():
    solution()

if __name__ == '__main__':
    main()