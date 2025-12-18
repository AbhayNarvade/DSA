from Node import Node

class SingleLinkedList :
    # constructor assign head none
    def __init__(self):
        self.head = None        
        self.length = 0
    # insertation at Beginning
    def insertAtBeginning(self, data):
        newnode = Node(data)
        newnode.setNext(self.head)
        self.head = newnode
        self.length +=1

    # insertion at ending
    def insertionAtEnding(self, data):
        if self.head is not None : 
            newnode = Node(data)
            current = self.head 
            while current.getNext() is not None :
                current = current.getNext()
            current.setNext(newnode)
            self.length +=1
        else :
            self.insertAtBeginning(data)

    # insertion at middel 
    def insertionAtMiddle(self,pos,data):
        if pos > self.length or pos < 0 :
            return None
        else :
            if pos == 0 :
                self.insertAtBeginning(data)
            else :
                if pos == self.length :
                    self.insertionAtEnding(data)
                else :
                    count = 0
                    current = self.head 
                    while count != (pos - 1) :
                        current = current.getNext() 
                        count +=1
                    newnode = Node(data)
                    newnode.setNext (current.getNext())
                    current.setNext(newnode)
                    self.length +=1

    # deletion at first node
    def deletionAtFirstNode(self):
        if self.length > 0 :
            self.head = self.head.getNext() 
            self.length -=1
        else :
            print('\n Linked List is empty')

    # deletion at last node
    def deletionAtLastNode(self):
        if self.length > 0 :
            if self.length == 1 :
                self.head = None
                self.length -=1
                return  
            current = self.head
            prev = None
            while current.getNext() is not None:
                prev = current
                current = current.getNext()
            
            prev.setNext(None)
            self.length -=1
        else :
            print('\n Linked List is empty ')

    # deletion by value 
    def deletionByValue(self,value):
        if self.head is None :
            print('\n Linked List is empty ')
        else :
            current = self.head
            prev = self.head
            if current.data == value :
                self.head = self.head.getNext()
                self.length -=1
                return 
            while current is not None and current.getData() != value:
                prev = current
                current= current.getNext()                
            
            if current is None:
                print('Value Not Found')
                return
            prev.setNext(current.getNext())
            self.length -=1

    # deletion at position
    def deleteAtPosition(self, pos):
        if self.head is None:
            print('\n Linked List is empty')
            return 
        else :
            if pos < 0 or pos >= self.length:
                print('\n Invalid Position')
                return
            if pos ==0 :
                self.head = self.head.getNext()
                self.length -=1
                return 
            

            current = self.head
            count = 0
            while count != (pos-1):
                current = current.getNext()
                count +=1
            
            NextElement = current.getNext()
            current.setNext(NextElement.getNext())
            self.length -=1

    # removed elements
    def removeElements(self, value):
        if self.head is None:
            return

        # Step 1: Remove matching head nodes
        while self.head and self.head.data == value:
            self.head = self.head.getNext()
            self.length -= 1

        if not self.head:
            return

        # Step 2: Remove non-head nodes
        current = self.head
        while current.getNext():
            if current.getNext().data == value:
                current.setNext(current.getNext().getNext())
                self.length -= 1
            else:
                current = current.getNext()

    # reverse single linked list 
    def reverseLinkedList(self):
        if self.head is None:
            print('reverse not posible because the head is None ')
            return
        
        if self.length ==1 :
            print('reverse not posible cause only one element are in Linked List')
            return
        
        prev = None
        current = self.head
        while current is not None:
            next = current.getNext()
            current.setNext(prev)
            prev = current
            current = next

        self.head = prev
    # Method for traversing 
    def traverseLinkedList(self):
        node = self.head

        while node : 
            print(node.getData() , end= " -> ")
            node = node.getNext()

        print('Total element in single linkedlist is ' , self.length)
        

ll = SingleLinkedList()

ll.insertAtBeginning(1)
ll.insertionAtEnding(2)
ll.insertionAtEnding(6)

ll.insertionAtEnding(3)
ll.insertionAtEnding(4)
ll.insertionAtEnding(5)
ll.insertionAtEnding(6)
ll.insertionAtEnding(6)
ll.insertionAtEnding(6)
# ll.insertionAtMiddle(3,40)

# ll.deletionAtFirstNode()
# ll.deletionByValue(400)
# ll.deleteAtPosition(2)

ll.removeElements(6)
ll.reverseLinkedList()



# node = ll.head

# while node : 
#     print(node.getData() , end= " -> ")
#     node = node.getNext()

# print('Total element in single linkedlist is ' , ll.length)
        