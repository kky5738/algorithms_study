import sys 

def solution():
    n = sys.stdin.readline().rstrip()
    s = n
    count = 0
    
    while True:
        if int(s) == int(n) and count != 0: break
        if int(s) < 10:
            s = s[-1] + s[-1]
        else:
            m = str(int(s[0]) + int(s[1]))
            s = s[1] + m[-1]
        count += 1

    print(count)

def main():
    solution()

if __name__ == '__main__':
    main()