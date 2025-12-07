from Node import Node

class circularLinkedList :
    def __init__(self):
        self.head = None
        self.length = 0

    def insertionAtBeginning(self, data ):
        newnode = Node(data)
        # if self.head is empty then this block of code will run
        if self.head is None :
            self.head = newnode
            newnode.setNext(self.head)
            self.length += 1
            return 
        # if self.head is not none that means there are element in list so what here we need to do is traverse
        else :
            current = self.head
            # Find the last node
            while current.getNext() != self.head:
                current = current.getNext()

            current.setNext(newnode)
            newnode.setNext(self.head)
            self.head = newnode
            self.length +=1
            return 
            
    def insertionAtEnd(self,data):
        if self.head is None :
            self.insertionAtBeginning(data)
            return 
        newnode = Node(data)
        current = self.head
        while current.getNext() != self.head:
            current = current.getNext()
        
        current.setNext(newnode)
        newnode.setNext(self.head)
        self.length += 1
    


    def insertionAtGivenPosition(self,position,data):
        if position <= self.length+1 and 0 < position   :
            if position == 1 :
                self.insertionAtBeginning(data)
                return 
            elif position == self.length+1:
                self.insertionAtEnd(data)
                return 
            else :
                current = self.head 
                count = 1 
                while count != (position-1):
                    current = current.getNext()
                    count +=1
                
                newnode = Node(data)
                nextElement = current.getNext()
                current.setNext(newnode)
                newnode.setNext(nextElement)
                self.length +=1 
                

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.getData(), end=" -> ")
            current = current.getNext()
            
            if current == self.head:   # stop when we come back to start
                break
        
        print("(back to head)")


c = circularLinkedList()
c.insertionAtBeginning(10)
c.insertionAtEnd(11)
c.insertionAtEnd(12)
c.insertionAtEnd(13)
c.insertionAtGivenPosition(2,14)
c.traverse()