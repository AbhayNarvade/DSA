# Implementation Thorough Linked List 

class Node :
    def __init__(self,data = None):
        self.data  = data 
        self.Next = None

class stackLinkedList:
    def __init__(self):
        self.top = None
        self.length = 0
    
    # is empty method 

    def isEmpty(self):
        return self.length == 0
    
    def push (self,item):
        newNode = Node(item)
        newNode.Next = self.top
        self.top = newNode
        self.length += 1
    
    def pop(self):
        if self.length == 0 :
            print('Stack Is Empty')
            return 
        returnData = self.top.data
        self.top = self.top.Next
        self.length -=1
        return returnData
            

    def peek(self):
        if self.top is not None :
            return self.top.data 
        print('Stack is empty ')



    def printStackData(self):
        current = self.top 
        while current is not None :
            print(f'[{current.data}]',end='->')
            current = current.Next
        print('\n')

if __name__ == '__main__':
    s =  stackLinkedList()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)



    s.printStackData()


    s.pop()
    s.pop()
    s.pop()


    s.printStackData()
