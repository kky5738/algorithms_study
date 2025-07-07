### 📌 오답 정리 - BOJ 5430 AC

## ❌ 내가 틀린 이유
- N이 최대 70만이기 때문에 O(N^2) 미만의 방법으로 접근해야 함
- R(reverse) 연산을 매번 직접 수행한다면 시간초과 발생
- 배열을 계속 뒤집지 않고, **R 연산의 횟수를 파악해 홀수번일 경우 마지막에 뒤집어야**함

---

## ✅ 올바른 접근
- R 연산을 직접 수행하지 않고 연산 횟수 파악 혹은 BOOL type을 이용해 실제 결과가 뒤집어진 경우 reverse 수행
- D 연산은 리스트 슬라이싱 대신 deque의 pop 연산 활용

---

## 💡 핵심 개념
1. **R(reverse) 연산 최적화** → 배열을 매번 직접 수정하는 대신 **연산 횟수만 저장 후 마지막에 수행**
2. **D(delete) 연산 최적화** → 리스트 슬라이싱 대신 pop 또는 popleft 연산 활용

---

## 📝 코드 비교

### ❌ 내 코드 (틀린 코드: 시간 초과)
```python
import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input() # 함수 리스트
    n = int(input()) # 배열 길이
    arr = input() # [a1, a2, ..., an] 형태의 정수 배열
    arr = arr[1:-1].split(",")
    if len(p) > n:
        print("error")
        continue
    
    r = 0
    for func in p:

        if func == "R":
            r += 1
            
        if func == "D":
            if r % 2 != 0:
                arr = arr[:-1]
            else:
                arr = arr[1:]
        
    if r % 2 != 0:
        arr = list(map(int, arr[::-1]))
    
    print(arr)
```
**🔴 문제점**
- R 연산은 잘 처리했으나 D 연산에서 시간 초과 발생
- line 37에서 함수 리스트 **p의 길이와 배열 길이 n만 비교하면** 모든 연산이 R로만 존재하는 케이스에서 오류 발생

---

### ✅ 정답 코드
```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input() # 함수 리스트
    n = int(input()) # 배열 길이
    arr = input() # [a1, a2, ..., an] 형태의 정수 배열
    arr = deque(arr.strip("[]").split(","))
    
    r = False
    try:
        for func in p:

            if func == "R":
                r = not r
                
            elif func == "D":
                if not arr or n == 0:
                    raise IndexError
                if r: # 뒤집어졌다면
                    arr.pop()
                else:
                    arr.popleft()
            
        if r:
            print(f"[{','.join(list(arr)[::-1])}]")
        else:
            print(f"[{','.join(arr)}]")
    except IndexError:
        print("error")
```


## 🔄 복습 필요 여부
- [x] 다시 풀어봐야 함
- [ ] 개념 복습 필요