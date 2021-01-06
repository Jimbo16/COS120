class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def get_stack(self):
        return self.items
    
    def top(self):
        return 
        
s = Stack()
print(s.isEmpty())
s.push(1)
s.push(6)
s.push(9)
s.push(22)
s.push(13)
s.push(18)
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.size())
print(s.isEmpty())