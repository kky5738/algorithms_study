import sys

S = set()

def add(x):
    global S
    if x not in S: S.add(x)

def remove(x):
    global S
    if x in S: S.remove(x)

def check(x):
    global S
    return print('1') if x in S else print('0')

def toggle(x):
    remove(x) if x in S else add(x)

def all():
    global S
    S = set([str(i) for i in range(1, 21)])

def empty():
    global S
    S = set()
    
function_dict = {
    'add': add,
    'remove': remove,
    'check': check,
    'toggle': toggle,
    'all': all,
    'empty': empty
}

m = int(input())

for _ in range(m):
    operation = sys.stdin.readline().rstrip().split()    
    if len(operation) == 2:
        function_dict[operation[0]](operation[1])
    else :
        function_dict[operation[0]]()
