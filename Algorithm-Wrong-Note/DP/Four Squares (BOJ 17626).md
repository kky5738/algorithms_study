# BOJ 17626 Four Squares

## ❌ 내가 틀린 이유
- DP 문제라는 것은 판단했지만, 점화식을 떠올리지 못함

## ✅ 올바른 접근
- 일반적인 경우, dp[i]는 1부터 i보다 작은 제곱수들을 활용해서 최소 개수를 찾는 과정이 필요함
- `dp[i] = min(dp[i - k^2] + 1) (단, k^2 ≤ i)`
- 즉, `i`에서 `k^2`을 뺀 값(`i - k^2`)을 만들 수 있는 최소 개수를 찾아 1을 더해주는 방식


## 💡 핵심 개념
- DP
- 수학적 성질 (라그랑주의 네 제곱수 정리)

## 📝 코드 비교
### ❌ 내 코드 (틀린 코드)
```python
 # 없음
```

### ✅ 정답 코드
```python
# BOJ 17626 Four Squrares
import sys

def solution(n:int) -> int:
    d = [0] * (n+1)
    d[1] = 1
    
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % int(i**0.5) == 0 and int(i**0.5) == i // int(i**0.5):
            d[i] = 1
            continue
        for j in range(2, int(i**0.5)+1):
            
            d[i] = min(d[i - j**2]+1, d[i])
    
    return d[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    
    answer = solution(n)
    print(answer)
```

## 🔄 복습 필요 유무
- [ ] 다시 풀어보야 함
- [x] 개념 복습 필요