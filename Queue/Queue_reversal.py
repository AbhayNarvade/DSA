
from Simple_Circular_Array import Queue

class QueueReverse (Queue):
        
    def QueueReveser(self):
        if self.isEmpty():
            return
        
        idx = self.front
        temp = []

        for i in range(self.count):
            temp.append(self.que[idx])
            idx = (idx + 1) % self.limit
        
        print('Without Reversing ' , self.que)
        temp.reverse()
        self.que = temp
        self.front = 0 
        self.rear = self.count
        print('With Reversing ' , temp)


# Testing reverse queue functionality 
if __name__ == '__main__':
    q = QueueReverse(5)
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50) # Queue is now full

    print('Front:', q.queueFront()) # Should be 10
    print('Rear:', q.queueRear())   # Should be 50
    q.QueueReveser()
    print('Front:', q.queueFront()) # Should be 50
    print('Rear:', q.queueRear())   # Should be 10