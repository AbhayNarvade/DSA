class Queue:
    def __init__(self, limit=5):
        self.limit = limit
        # Pre-allocate the list with None to act as a fixed-size array
        self.que = [None] * limit
        self.front = 0
        self.rear = 0
        self.count = 0  # To track current number of elements

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.limit

    def enQueue(self, item):
        if self.isFull():
            print('Queue Overflow')
            return 
        
        # Calculate position using modulo for wrap-around
        self.que[self.rear] = item
        self.rear = (self.rear + 1) % self.limit
        self.count += 1
        print(f'Enqueued {item}. Current Queue state: {self.que}')

    def deQueue(self):
        if self.isEmpty():
            print('Queue Underflow')
            return 
        
        removed = self.que[self.front]
        self.que[self.front] = None  # Optional: clear the slot
        
        # Move front pointer forward with wrap-around
        self.front = (self.front + 1) % self.limit
        self.count -= 1
        
        print(f'Removed {removed}.')
        return removed

    def queueFront(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.que[self.front]

    def queueRear(self):
        if self.isEmpty():
            return "Queue is empty"
        # Rear pointer is always one step ahead, so we go back one
        return self.que[(self.rear - 1) % self.limit]

    def size(self):
        return self.count

# Testing the Circular Logic
if __name__ == '__main__':
    q = Queue(5)
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50) # Queue is now full
    
    q.deQueue()   # Removes 10, index 0 is now "empty"
    q.enQueue(60) # Wraps around and puts 60 into index 0
    
    print('Front:', q.queueFront()) # Should be 20
    print('Rear:', q.queueRear())   # Should be 60

