class Stack:
    def __init__(self):
        self.stack=[]
        self.index=0
    def empty(self):
        return self.stack==[]
    def push(self,data):
        self.stack.insert(self.index,data)
        self.index+=1
        print("{} is pushed int the stack".format(data))
    def pop(self):
        self.index-=1
        d=self.stack.pop(self.index)
        print("{} is pop from stack".format(d))
    def size(self):
        return len(self.stack)
if __name__=="__main__":
    s=Stack()
    i=1
    while i<5:
        l=int(input("enter the elements to push:"))
        s.push(l)
        i+=1
    print(s.size())
    s.pop()
    s.pop()
    s.pop()
    print(s.size())






