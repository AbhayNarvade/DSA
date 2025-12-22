# Simple Array Implementation of Slack 

class Stack :
    def __init__(self, limit =10):
        self.stk = []
        self.limit = limit 

    def isEmpty(self):
        return len(self.stk)<=0
    
    def push (self,item):
        if len(self.stk) >= self.limit:
            print ("Stack is Overflow")
        else :
            self.stk.append(item)
            print ('Stack after push ', self.stk)

    def pop(self):
        if len(self.stk)<=0:
            print ('Stack Underflow')
            return 0
        else :
            return self.stk.pop()
        
    def peek (self):
        if len(self.stk)<=0:
            print('Stack Underflow')
            return 0
        else :
            return self.stk[-1]
        

    def size (self):
        return len(self.stk)
    


s = Stack(5)

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print( 'This is an peek',s.peek())
print('this is and pop element', s.pop())
print( 'This is an peek',s.peek())
print('this is and pop element', s.pop())
print( 'This is an peek',s.peek())
print('this is and pop element', s.pop())
print( 'This is an peek',s.peek())
