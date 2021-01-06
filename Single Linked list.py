import random as rnd
class Node:
   def __init__(self, data):
        self.data = data
        self.next = None
def creatLinkedList(n):
    head = Node(rnd.random())
    cur = head
    for i in range(1, n):
        cur.next = Node(rnd.random())
        cur = cur.next
    return head

def readLinkedList(head):
    cur = head
    while cur is not None:
        print(cur.data, end =",")
        cur = cur.next
        
def searchLinkedList(head, target):
    cur = head
    while cur is not None:
        if (cur.data != target):
            cur = cur.next
        elif(cur.data == target):
            return True
    return False

def addStartNode(head,data):
    newNode = Node(data)
    newNode.next = head.next
    head = newNode
    return False

def removeNode(head, target):
     cur = head
     while cur is not None:
        if (cur.data != target):
            cur = cur.next
        elif(cur.data == target):
            head.next = cur.next
            cur = cur.next
            print(f"The target value {target.data} is successfully deleted")
            return head
     print(f"The target value ")
a = creatLinkedList(5)
print(a.data)
readLinkedList(a)
searchLinkedList(a,0.9303938682261708)
addStartNode(a,10)
removeNode(a,0.43678787719170953)
