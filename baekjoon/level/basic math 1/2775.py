import sys

def solution():
    zero = [i for i in range(1, 15)]
    def recul(sum:list, n, f, end):
        if f == end: return sum
        
        result = []
        for i in range(1, n+1):
            temp = 0
            for j in range(i):
                temp += sum[j]
            result.append(temp)
        f += 1
        return recul(result, n, f, end)
    
    n_test_case = int(sys.stdin.readline().rstrip())
    for _ in range(n_test_case):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())

        answer = recul(zero, n, f=0, end=k)
        print(answer[n-1])

if __name__ == '__main__':
    solution()