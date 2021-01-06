class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def isEmpty(self):
        if self.isEmpty == None:
            return True
        else:
            return False
        
    def EnQueue(self, data):
        newNode = Node(data)
        if self.isEmpty is None:
            self.rear = self.front = newNode
        else:
            cur = self.front
            newNode.next = cur
            self.front = newNode
            
    def DeQueue(self):
        if self.isEmpty is None:
            print("Queue is empty")
            
        else:
            cur = self.front
            temp = cur.next
            cur = None
            self.front = temp
            
    def display(self):
        cur = self.front
        if self.isEmpty():
            print("Queue Underflow")
        else:
            while cur != None:
                print(cur.data)
                cur = cur.next
            return
        
q = Queue() 
q.EnQueue(10)
q.DeQueue()
q.display()