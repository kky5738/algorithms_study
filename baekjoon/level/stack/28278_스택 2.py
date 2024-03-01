import sys

stack = []

def oper1(x):
    stack.append(x)

def oper2():
    if len(stack) != 0: print(stack.pop())
    else: print(-1)

def oper3():
    print(len(stack))

def oper4():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def oper5():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)

n = int(sys.stdin.readline().rstrip())

oper_dict = {
    '1': oper1,
    '2': oper2,
    '3': oper3,
    '4': oper4,
    '5': oper5
}

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    
    if command[0] == '1':
        oper_dict[command[0]](command[1])
    else:
        oper_dict[command[0]]()