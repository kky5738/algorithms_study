import sys
from collections import Counter

def solution():
    num = list(map(int, sys.stdin.readline().split(' ')))
    num.sort(reverse=True)

    cnt = Counter(num).most_common()
    
    prize = cnt[0][0]
    print(prize*1000 + 10000 if len(cnt) == 1 else prize * 100 + 1000 if len(cnt) == 2 else prize * 100)
    # len(cnt) == 1 -> 모든 수가 같은 경우
    # len(cnt) == 2 -> 2개가 같은 경우
    # len(cnt) == 3 -> 모든 수가 다른 경우
    

def main():
    solution()

if __name__ == "__main__":
    main()