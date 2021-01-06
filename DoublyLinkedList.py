class DLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DLL:
    head = None
    tail = None
    
    def __init__(self, node):
        self.head = self.tail = node
    
    def addTail(self, data):
        temp = DLNode(data)
        self.tail.next = temp
        self.tail = temp
        
    def addHead(self,data):
        newNode = DLNode(data)
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode
        
    def removeHead(self, data):
        cur = self.head
        temp = cur.next
        cur.next = None
        temp.prev = None
        cur = None
        self.head = temp
        
    def deleteNode(self, target, data):
        cur = self.head
        while cur is not None:
            if cur.data != target:
                cur = cur.next
            elif cur.data == target:
                temp = cur.next
                temp.next = cur.next
                
                
    def addNode(self, target,data):
        newNode = DLNode(data)
        cur = self.head
        while cur is not None:
            if cur.data != target:
                cur = cur.next
            elif cur.data == target:
                temp = cur.next
                temp.next = newNode.next
                newNode.prev = cur
                cur.next = newNode
        
        
    def removeTail(self, data):
        cur = self.tail
        temp = cur.prev
        cur = None
        self.tail = temp
        
        
        
        
    def searchTarget(self, target, data):
        found = False
        cur = self.head
        while cur is not self.tail and cur.data is not target:
            cur = cur.next
            if cur.data == target:
                found = True
                
            if found == True:
                print("Found")
            else:
                print("Not found")
                
    def traverseForward(self):
        cur = self.head
        print(cur.data)
        while cur is not self.tail:
            cur = cur.next
        print(cur.data)
        
     
            
s = DLL(DLNode(10))
s.addTail(9)
s.addTail(7)
s.addHead(8)
s.removeHead(10)
s.removeTail(8)
s.removeHead(9)
s.traverseForward()
