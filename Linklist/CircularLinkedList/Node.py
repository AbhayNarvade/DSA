class Node :
    #constructor to intiliase the node
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 
    # setting the data
    def setData(self, data):
        self.data = data
    # getting the data
    def getData(self):
        return self.data
    # setting the next element
    def setNext(self,next):
        self.next = next
    # getting the next element 
    def getNext(self):
        return self.next
    # Return true if node point to another node
    def hasNext(self):
        return self.next !=None

