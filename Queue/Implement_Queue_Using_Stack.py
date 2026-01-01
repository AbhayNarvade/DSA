# Implement Queue using stack 

class Queue :
    # constructor
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Element added at the end in stack 1 
    def enqueue(self, item):
        self.stack1.append(item)

    # Element start removing from stack 2 
    def dequeue(self):
        if not self.stack2 :
            while len(self.stack1) > 0 :
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def printQueue(self):
        queue = []
        queue.extend(self.stack2)
        queue.extend(self.stack1)
        print("Queue (front → rear):", queue)

if __name__ == '__main__':        

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())  
    q.enqueue(40)
    print(q.dequeue())  
    q.enqueue(50)
    q.enqueue(60)
    
    q.printQueue() 

    # output
    # 10
    # 20
    # Queue (front → rear): [30, 40, 50, 60]