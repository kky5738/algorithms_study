n = int(input())
answer = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # if '3' in str(i) + str(j)  + str(k) -> 이 조건으로 풀면 좀 더 간단한 코드 구현 가능
            if '3' in str(k):
                answer += 1
                continue
            if '3' in str(j):
                answer += 1
                continue
            if '3' in str(i):
                answer += 1

print(answer)