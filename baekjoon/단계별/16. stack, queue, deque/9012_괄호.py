import sys

def solution(round: str):
    cnt = 0
    
    for r in round:
        if cnt < 0:
            return "NO"
        if r == "(":
            cnt += 1
        elif r == ")":
            cnt -= 1
    
    return "NO" if cnt != 0 else "YES"

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        round = sys.stdin.readline().rstrip()
        result = solution(round)
        print(result)