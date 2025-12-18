from SingleLinkedList import SingleLinkedList 
from Node import Node

l1 = SingleLinkedList()

l1.insertAtBeginning(1)
l1.insertionAtEnding(2)
l1.insertionAtEnding(3)
l1.insertionAtEnding(4)
l1.insertionAtEnding(5)
l1.insertionAtEnding(6)


node = l1.head
secondNode = None

while node : 
    if node.getData() == 2 :
        secondNode = node
    print(node.getData() , end= " -> ")
    node = node.getNext()


print('Total element in single linkedlist is ' , l1.length)

# print("secondNode ", secondNode.getData())



#  Delete Node By given Node

def deleteNodeByGivenNode(node):
    if node is None or node.getNext() is None:
        return False
    
    temp = node.getNext()
    node.setData(temp.getData())
    node.setNext(temp.getNext())

    del temp


deleteNodeByGivenNode(secondNode)


node = l1.head
secondNode = None

while node : 
    if node.getData() == 2 :
        secondNode = node
    print(node.getData() , end= " -> ")
    node = node.getNext()
print('Total element in single linkedlist is ' , l1.length-1)
