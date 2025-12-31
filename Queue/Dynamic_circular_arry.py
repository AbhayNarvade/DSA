# Dynamic Circular Array 
class DynamicQueue :
    # Constructor 

    def __init__(self , capacity = 4 ):
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0 
        self.que = [None] * capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.rear = (self.rear + 1 ) % self.capacity
        self.que[self.rear] = item
        self.size += 1

    def dequeue (self):
        if self.isEmpty() :
            print('Queue is Underflow')
            return 

        removedElement = self.que[self.front]
        self.que[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -=1

        if self.size <= self.capacity // 4 and self.capacity >4:
            self._resize(self.capacity // 2)
            
        return removedElement
    
    def getFront(self):
       if self.que[self.front] is not None :
            print(f'Front is {self.que[self.front]}')
        
    def getRear(self):
       if self.que[self.rear] is not None :
            print(f'Rear is {self.que[self.rear]}')     

    def isFull(self):
        return self.capacity == self.size
    
    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        return str(self.que)
    

    def _resize(self,NewCapcity):
        newNode = [None] * NewCapcity
        for i in range(self.size):
            newNode[i] = self.que[(self.front + i) % self.capacity]

        self.que = newNode 
        self.front = 0 
        self.rear = self.size - 1
        self.capacity = NewCapcity
        


if __name__ =='__main__':

    d = DynamicQueue()
    d.enqueue(1)
    d.enqueue(2)
    d.enqueue(3)
    d.dequeue()
    d.dequeue()
    d.dequeue()
    d.enqueue(21)
    d.enqueue(22)
    d.enqueue(23)
    d.enqueue(24)
    d.enqueue(25)
    d.enqueue(26)
    d.enqueue(27)
    d.enqueue(28)
    d.enqueue(29)
    d.enqueue(30)
    d.dequeue()
    d.dequeue()
    d.dequeue()
    d.dequeue()
    d.dequeue()
    d.dequeue()
    d.getFront()
    d.getRear()
    print(d)