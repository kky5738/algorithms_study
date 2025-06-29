import sys

class Queue:
    def __init__(self):
        self.q = []
        
    def push(self, x):
        x = int(x[1])
        self.q.append(x)
    
    def pop(self, x):
        if self.q: # q가 존재하고 비어있지 않다면 true 반환
            print(self.q[0])
            self.q = self.q[1:]
            
        else: # q가 비었을 경우
            print(-1)
    
    def size(self, x):
        print(len(self.q))
    
    def empty(self, x):
        print(int(not(bool(self.q))))
    
    def front(self, x):
        if self.q:
            print(self.q[0])
        else:
            print(-1)
            
    def back(self, x):
        if self.q:
            print(self.q[-1])
        else:
            print(-1)

class Operator:
    def __init__(self, q: Queue):
        self.Q = q
        
        self.func_dict = {'push': self.Q.push,
                 'pop': self.Q.pop,
                 'size': self.Q.size,
                 'empty': self.Q.empty,
                 'front': self.Q.front,
                 'back': self.Q.back}
    
    def parse(self, data: str):
        data = data.split()
        self.func_dict[data[0]](data)
        


if __name__ == "__main__":
    q = Queue()
    op = Operator(q)
    
    input = sys.stdin.readline
    n = int(input().rstrip())
    
    for _ in range(n):
        data = input().rstrip()
        op.parse(data)
