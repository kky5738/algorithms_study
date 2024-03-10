# 백준 기하: 직사각형과 삼각형 10101번 삼각형 외우기

angle=[]
for i in range(3):
    a = int(input())
    angle.append(a)

answer = ''
if sum(angle) != 180:
    answer='Error'

else:
    angle = list(set(angle))
    answer = 'Equilateral' if len(angle)==1 else 'Isosceles' if len(angle)==2 else 'Scalene' 

print(answer)