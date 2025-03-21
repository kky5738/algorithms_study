# BOJ 17608 막대기
import sys

def solution():
    input = sys.stdin.readline
    
    n = int(input().rstrip())
    sticks = []
    
    answer = n # 숫자를 비교하며 가려지는 수가 생길 때마다 n-1
    
    for _ in range(n):
        sticks.append(int(input().rstrip()))
        
    criteria = sticks.pop() # 맨 오른쪽 숫자를 기준으로 설정
    
    for _ in range(n-1):
        current = sticks.pop()
        if current <= criteria: # 현재 수가 오른쪽에 있는 수에 가려질 때
            answer -= 1
        if current > criteria: # 현재 수가 오른쪽에 있는 수보다 클 때 기준을 변경
            criteria = current
            
    print(answer)

if __name__ == "__main__":
    solution()