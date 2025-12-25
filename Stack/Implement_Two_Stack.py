# Implement Two Stack in One Array 

class TwoStacks :
    def __init__(self, limit =10):
        self.stk = [None] * limit
        self.top1 = -1 
        self.top2 = limit
        self.limit = limit
    def push1 (self, item ):
        if self.top1< self.top2 -1 :
            self.top1 +=1
            self.stk[self.top1] = item
        else :
            print("Stack1 Overflow")
    def push2 (self,item):
        if self.top1 < self.top2 -1 :
            self.top2 -=1
            self.stk[self.top2] = item
        else :
            print("Stack2 Overflow")
    
    def pop1(self):
        if self.top1 >= 0 :
            x = self.stk[self.top1]
            self.stk[self.top1] = None
            self.top1 -=1
            return x
        return -1 

    def pop2(self):
        if self.top2 < self.limit:
            x = self.stk[self.top2]
            self.stk[self.top2] = None
            self.top2 +=1
            return x
        else:
            return -1


if __name__ == '__main__':
    s = TwoStacks(10)
    s.push1(2)
    s.push1(3)
    s.push2(4)
    print(s.pop1(),end=' ')
    print(s.pop2(),end=' ')
    print(s.pop2(),end=' ')
    print('\n')