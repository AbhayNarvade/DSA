class Node :
    # Constructor
    def __init__(self , data = None , next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    # Method of Setting the data field of the node
    def setData(self,data):
        self.data = data
    # Method of Getting the data field of the node
    def getData(self):
        return self.data
    # Method of Setting the Next field of the node
    def setNext(self,next):
        self.next = next
    # Method of Getting the Next field of the node
    def getNext(self):
        return self.next
    # Return true if the Node points to another node
    def hasNext(self):
        return self.next != None
    # Method of Setting the Prev field of the node
    def setPrev(self,prev):
        self.prev = prev
    # Method of Getting the Prev field of the node
    def getPrev(self):
        return self.prev
    # Return true if the Node points to another node
    def hasPrev(self):
        return self.prev != None
    
    def __str__(self):
        return f"Node({self.data} , {self.next} , {self.prev})"