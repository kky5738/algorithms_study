# BOJ 6571 피보나치 수의 개수. 큰 수를 어떻게 다뤄야 할지 모르겠어 ChatGPT 도움을 받음
import sys

def solution():
    import bisect
    # 근데 이 코드도 전체 테스트 케이스는 통과하지 못함.. 아마 bisect 라이브러리 문제?
    
    # 피보나치 수를 10^100 이하까지 미리 계산. dp 테이블을 10^100 크기로 할당하면 메모리 초과.
    fibonacci = [1, 1]
    while True:
        next_fibo = fibonacci[-1] + fibonacci[-2]
        if next_fibo > 10**100: # 10^100을 넘으면 종료
            break
        fibonacci.append(next_fibo)
    
    # 이진 탐색을 사용하여 범위 [a, b]에 포함된 개수 찾기
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        
        if a == 0 and b == 0: break
        
        left = bisect.bisect_left(fibonacci, a) # a 이상의 첫번째 위치
        right = bisect.bisect_right(fibonacci, b) # b 이하 마지막 위치 + 1
        
        print(right - left)

# -----------------------------------------------------------------------------------------
# 아래는 GPT가 만든 코드

def generate_fibonacci():
    """ 10^100 이하의 피보나치 수를 리스트에 저장 """
    fib = ["1", "2"]  # f1 = 1, f2 = 2 (문자열로 저장)
    
    while True:
        next_fib = str(int(fib[-1]) + int(fib[-2]))  # 문자열 덧셈 후 변환
        if len(next_fib) > 101:  # 10^100을 초과하면 중단
            break
        fib.append(next_fib)
    
    return fib

def count_fibonacci_in_range(a: str, b: str, fib_list):
    """ a, b 범위 내 피보나치 수 개수 찾기 (문자열 비교 활용) """
    def lower_bound(fib_list, x):
        """ x 이상이 처음 나타나는 위치 찾기 (이진 탐색) """
        left, right = 0, len(fib_list)
        while left < right:
            mid = (left + right) // 2
            if int(fib_list[mid]) >= int(x):  # 큰 수 비교를 위해 int 변환
                right = mid
            else:
                left = mid + 1
        return left
    
    def upper_bound(fib_list, x):
        """ x 초과가 처음 나타나는 위치 찾기 (이진 탐색) """
        left, right = 0, len(fib_list)
        while left < right:
            mid = (left + right) // 2
            if int(fib_list[mid]) > int(x):
                right = mid
            else:
                left = mid + 1
        return left
    
    start = lower_bound(fib_list, a)
    end = upper_bound(fib_list, b)

    return end - start



if __name__ == "__main__":
    # solution()
    
    # ✅ 피보나치 수 미리 계산
    fib_list = generate_fibonacci()

    # ✅ 입력 처리
    input = sys.stdin.read
    data = input().strip().split("\n")

    for line in data:
        a, b = line.split()
        if a == "0" and b == "0":
            break
        print(count_fibonacci_in_range(a, b, fib_list))