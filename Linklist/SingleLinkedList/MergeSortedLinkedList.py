from SingleLinkedList import SingleLinkedList 
from Node import Node

l1 = SingleLinkedList()

l1.insertAtBeginning(1)
l1.insertionAtEnding(2)
l1.insertionAtEnding(3)

l2 = SingleLinkedList()

l2.insertAtBeginning(1)
l2.insertionAtEnding(4)
l2.insertionAtEnding(5)

node = l1.head

while node : 
    print(node.getData() , end= " -> ")
    node = node.getNext()

print('Total element in single linkedlist is ' , l1.length)
        
node = l2.head

while node : 
    print(node.getData() , end= " -> ")
    node = node.getNext()

print('Total element in single linkedlist is ' , l2.length)


def MergeSortedLinkedList(Linked1,Linked2):
        MergeLinkedList = SingleLinkedList()

        dummy = Node(0)

        current = dummy

        l1 = Linked1.head
        l2 = Linked2.head

        while l1 and l2:
            if l1.getData() <= l2.getData():
                current.setNext(l1)
                l1=l1.getNext()
            else :
                current.setNext(l2)
                l2 = l2.getNext()

            current = current.getNext()

        current.setNext( l1 if l1 else l2 )

        MergeLinkedList.head = dummy.getNext()
        MergeLinkedList.traverseLinkedList()



MergeSortedLinkedList(l1,l2)

