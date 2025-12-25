# Implement Stack using Queues
from collections import deque

class Mystack():
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        self.q2.append(x)

        while self.q1:
            element = self.q1.popleft()
            self.q2.append(element)

        self.q1 , self.q2  = self.q2 , self.q1

    
    def pop (self):
        if self.isEmpty():
            return -1
        return self.q1.popleft()
    

    def top (self):
        if self.isEmpty():
            return -1
        return self.q1[0]

    def isEmpty(self):
        return len(self.q1) == 0

if __name__ == "__main__":
    stack = Mystack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())