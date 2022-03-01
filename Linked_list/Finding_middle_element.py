
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    
    def __init__(self,data):
        self.head = data

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
    
    def middle(self):
        # slow = fast = self.head

        # while(fast and fast.next):
        #     slow = slow.next
        #     fast = fast.next.next
        
        # return slow.data

    #Method 2 for middle element:
        arr = [self.head]
        while(arr[-1].next):
            arr.append(arr[-1].next)
        
        return arr[len(arr)//2].data
        

    def print(self):
        head = self.head
        while(head):
            print(head.data,end=" ")
            head = head.next
    
        print(self.head)

llist = Linkedlist(0)
llist.push(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.print()
print("The middle element is ",llist.middle())
