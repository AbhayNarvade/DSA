# Remove Duplicates from an Unsorted Linked List

from Node import Node
from SingleLinkedList import SingleLinkedList



class Removed_Duplicate(SingleLinkedList):
    #  Remove Duplicates from an Unsorted Linked List Using HashMap 
    def Removed_Duplicate_entries(self):
        s = set()
        prev = Node()
        first = prev
        current = self.head

        while current is not None:
            if current.getData() not in s :
                s.add(current.getData())
                prev.setNext(current)
                prev = current
            else :
                self.length -= 1
            current = current.getNext()
        
        prev.setNext(None)

        self.head = first.getNext()




l1 = Removed_Duplicate()
l1.insertAtBeginning(10)
l1.insertionAtEnding(30)
l1.insertionAtEnding(20)
l1.insertionAtEnding(40)
l1.insertionAtEnding(30)
l1.insertionAtEnding(40)

l1.Removed_Duplicate_entries()




node = l1.head

while node : 
    print(node.getData() , end= " -> ")
    node = node.getNext()

print('Total element in single linkedlist is ' , l1.length)
