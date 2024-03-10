# 백준 9020번 골드바흐의 추측
# 풀긴 했지만 실행시간 줄여보기
import sys
from math import ceil
from itertools import combinations

def main():
    solution()

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        
        # N까지 소수 구하기
        prime = prime_list(n)

        # n/2가 소수인 경우 n/2 + n/2가 골드바흐 파티션임
        if int(n/2) in prime:
            print(int(n/2), int(n/2))
            continue

        # 조합을 만들 경우의 수를 줄여 시간초과 방지
        if len(prime) < 500:
            temp = prime
        else:
            temp = [x for x in prime if x > int(n / 2) - ceil(n / 10)+1 and x < int(n / 2) + ceil(n / 10)+1]
        
        # 소수 리스트에서 2개 원소 택해서 조합 만들기
        comb_prime = list(combinations(temp, 2))

        # 두 수의 차이를 저장하기 위한 변수
        min = n

        # 정답을 저장하기 위한 변수
        ans = 0

        # 소수 조합 중 두 수의 합이 n이 되는 값만 리스트에 저장
        for x in comb_prime:
            if x[0] + x[1] == n and abs(x[0] - x[1]) < min:
                min = abs(x[0] - x[1])
                ans = [x[0], x[1]]
        
        # 오름차순 정렬
        ans.sort()

        # 정답 출력
        print(ans[0], ans[1])

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n + 1) if sieve[i] == True]

if __name__ == '__main__':
    main()