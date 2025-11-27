class Node :
    #constructor 
    def __init__(self, data = None):
        self.data = data
        self.next = None
    # method for setting the data fields in node
    def setData(self,data):
        self.data = data
    # method for getting the data fields of the node
    def getData(self):
        return self.data
    # method for setting the next fields of the node
    def setNext(self, next):
        self.next = next
    # method for getting the next fields of the node 
    def getNext(self):
        return self.next
    # return true if the node points to another node
    def hasNext(self):
        return self.next != None 

    
