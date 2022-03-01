

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    
    def __init__(self):
        self.head = None

    def push(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def append(self, data):
        new_data = Node(data)
        
        if self.head is None:
            self.head = new_data
            return 
        
        head = self.head
        while(head.next):
            head = head.next
        
        head.next = new_data

    def print(self):
        head = self.head
        while(head):
            print(head.data,end=" ")
            head = head.next
    

llist = Linkedlist()
llist.push(1)
llist.append(2)
llist.print()
