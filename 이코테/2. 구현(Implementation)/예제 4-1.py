import sys

n = int(sys.stdin.readline().rstrip())
plans = sys.stdin.readline().rstrip().split()
answer = [1,1]
dict_plan = {'L': (1, -1), 'R': (1, 1), 'U': (0, -1), 'D': (0, 1)}

def move(answer, plan):
    idx, coor = dict_plan[plan]
    temp = answer[idx]
    answer[idx] += coor
    
    if answer[idx] == 0 or answer[idx] > n:
        answer[idx] = temp
        return answer
    else:
        return answer

for plan in plans:
    answer = move(answer, plan)

print(answer[0], answer[1])