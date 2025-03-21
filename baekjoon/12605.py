# BOJ 12605 단어순서 뒤집기
import sys

def solution(n: int, strings: list[str]):
    result = []
    for i in range(n):
        result.append([strings[i].pop() for _ in range(len(strings[i]))]) # stack의 pop 연산을 통해 뒤집기
        
    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    strings = [list(input().rstrip().split()) for _ in range(n)]
    
    result = solution(n, strings)
    for i in range(n):
        print(f'Case #{i+1}: {" ".join(result[i])}')