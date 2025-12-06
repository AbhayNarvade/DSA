from Node import Node

class doubleLinkedList : 
    # constructor 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def insertAtBeginning (self,data):
        newnode = Node(data)
        if self.head==None:
            self.head = self.tail = newnode
        else:
            newnode.setPrev(None)
            newnode.setNext(self.head)
            self.head.setPrev(newnode)
            self.head = newnode
        self.length += 1

    def insertAtEnding(self,data):
        if self.tail == None:
            self.insertAtBeginning(data)
            return
        else :
            newnode = Node(data)
            newnode.setPrev(self.tail)
            newnode.setNext(None)
            self.tail.setNext(newnode)
            self.tail = newnode
            self.length += 1

    def insetionAtGivenPosition(self,postion,data):
        if postion <=self.length and postion > 0 :
            if postion == 1 :
                self.insertAtBeginning(data)
                return
            elif postion == self.length  :
                self.insertAtEnding(data)
                return
            else :
                current = self.head
                count = 1
                while count != (postion-1):
                    current = current.getNext()
                    count +=1
                
                newnode = Node(data)
                nextelement = current.getNext()
                newnode.setNext(nextelement)
                newnode.setPrev(current)
                current.setNext(newnode)
                nextelement.setPrev(newnode)
                self.length +=1

    def removedElementAtBeginning(self):
        if self.head is None:
            return 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return 
        
        else :
            current = self.head
            current = current.getNext()
            current.setPrev(None)
            self.head  = current
            self.length -=1

    def removedElementAtEnd(self):
        if self.tail is None:
            return 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return
        else :
            lastElement = self.tail
            secondLastElement = lastElement.getPrev()
            secondLastElement.setNext(None)
            self.tail = secondLastElement
            self.length -=1

    def removedElementAtGivenPosition(self,position):
        if position>0 and  position <= self.length:
            if position == 1:
                self.removedElementAtBeginning()
                return 
            if position == self.length:
                self.removedElementAtEnd()
                return 
            else :
                current = self.head
                count = 1
                while count != (position-1):
                    current = current.getNext()
                    count +=1
                nodeToRemoved = current.getNext()
                nextElement = nodeToRemoved.getNext()
                current.setNext(nextElement)
                
                if nextElement:
                    nextElement.setPrev(current)
                else :
                    # If nextNode is None, then current becomes new tail
                    self.tail = current
                
                self.length -=1


    def getAllElement(self):
        if self.head is None:
            return 
        else:
            current = self.head
            print(f'Total element in doubleLinkedList are {self.length} and Element inside doubleLinkedList',end='\n <->')
            while current is not None:
                print(current.getData(),end= "<->")
                current = current.getNext()
            print('\n')
            


ll = doubleLinkedList()
ll.insertAtBeginning(10)
ll.insertAtEnding(11)
ll.insertAtEnding(12)
ll.insertAtEnding(13)
ll.insertAtEnding(14)
ll.insetionAtGivenPosition(5,5)
ll.removedElementAtEnd()
ll.removedElementAtBeginning()
ll.removedElementAtGivenPosition(3)

ll.getAllElement()