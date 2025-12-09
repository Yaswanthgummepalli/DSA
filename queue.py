class Queue:
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)
        print(f"{data} is inserted to queue")
    def dequeue(self):
        a=self.queue.pop(0)
        print("{}element is removed".format(a))
    def size(self):
        return len(self.queue)
    def print(self):
        print(self.queue)
if __name__=="__main__":
    q=Queue()
    print(q.isempty())
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(4)
    q.print()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.print()
    print("queue size is",q.size())
    q.enqueue(6)
    q.print()
