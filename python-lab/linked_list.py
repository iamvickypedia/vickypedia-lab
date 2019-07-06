class Node:
    def __init__(self,data,target=None):
        self.data = data
        self.next = target

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertFirst(self,data):
        self.head = Node(data,target = self.head)
        self.size += 1
    def insertLast(self,data):
        node = Node(data)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.size += 1

    def printAll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

ll = LinkedList()
import pdb;pdb.set_trace()

ll.printAll()
