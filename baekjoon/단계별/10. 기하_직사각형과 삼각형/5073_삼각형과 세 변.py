# 백준 기하: 직사각형과 삼각형

answer_dict = {'1': 'Equilateral',
          '2': 'Isosceles',
          '3': 'Scalene'}
while True:
    answer = ''
    x = list(map(int, input().split()))
    
    if sum(x) == 0: break
    
    x = sorted(x)
    if sum(x[:2]) <= x[-1]:
        answer = 'Invalid'
    else:
        key = str(len(set(x)))
        answer = answer_dict[key]
    print(answer)