import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    answer = 0
    
    if n % 5 == 0:
        answer += n//5
        n %= 5
        
    else:
        cnt = 0
        result = n
        while True:
             if result % 3 == 0 and result <= 12: break
             result -= 5
             cnt += 1
        if result < 0: result = cnt*5 + n
        answer += (n-result) // 5
        
        answer += result // 3
        result %= 3
        n = result

    print(answer if n==0 else -1)

if __name__ == '__main__':
    solution()