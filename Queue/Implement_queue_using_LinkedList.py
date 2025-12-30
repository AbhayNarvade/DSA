class Node :
    # constructor 

    def __init__(self , data = None):
        self.data = data
        self.next = None

class Queue :
    #  constructor

    def __init__(self):
        self.head =None
        self.tail = None
    
    # Insert Element in Queue 
    def enqueue (self ,item):
        newNode = Node(item)
        if self.head is None :
            self.head = self.tail  = newNode
            return 
        else :
            self.tail.next = newNode
            self.tail = newNode
            return 
    
    def dequeue (self):
        if self.head is None :
            return print('Queue is empty')
        if self.head.next is None :
            popelement = self.head.data
            self.head , self.tail = None
            return print('popelement ', popelement)
        
        popelement = self.head.data
        self.head = self.head.next
        return print('popelement ', popelement)
    
    def frontElement(self):
        if self.head is None:
            print('Queue is empty')
        else:
            print('front element is', self.head.data)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)
    q.enqueue(35)
    q.enqueue(45)

    q.dequeue()
    q.frontElement()
    q.dequeue()
    q.frontElement()
    q.dequeue()
    q.frontElement()


