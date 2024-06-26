# 반복문을 사용한 팩토리얼
def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

# 재귀 함수를 사용한 팩토리얼
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))