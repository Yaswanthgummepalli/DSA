

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def after_element(self,data,x):

        n=self.head
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("element is not found")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def before_element(self,data,x):
        if self.head is None:
            print("linked list is empty")
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("element is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node

        else:
            print("go for other insertions")
    def isempty(self):
        if self.head is None:
            print("list is empty")
        else:
            print("list is not empty")
    def delete_at_begin(self):
        if self.head is None:
            print("list is empty-delete at begin")
        else:
            self.head=self.head.ref
    def delete_at_end(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_at_middle(self,x):
        if self.head is None:
            print("list is empty")
        else:
            if self.head.data==x:
                self.head=self.head.ref
            else:
                n=self.head
                while n.ref is not None:
                    if n.ref.data==x:
                        break
                    n=n.ref
                if n.ref is None:
                    print("element is not found")
                else:
                    n.ref=n.ref.ref

l=Linkedlist()
l.add_begin(34)
l.add_begin(23)

l.add_last(45)

l.before_element(12,34)

l.delete_at_begin()
l.print_linkedlist()





