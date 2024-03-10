# 백준 기하:직사각형과 삼각형 9063번 대지
n = int(input())

x_list = []
y_list = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

width = abs(max(x_list) - min(x_list))
height = abs(max(y_list) - min(y_list))

print(width * height)