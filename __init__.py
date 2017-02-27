from linkedlist import LinkedList
from linkedlist.node import LinkedListNode  



class Stack:

    def __init__(self):
        self.items = LinkedList()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            current = self.items.head
            while current.next != None:
                current = current.next
            return self.items.remove(current.value).value

    def peek(self):
        if self.size() == 0:
            return None
        else:
            current = self.items.head
            while current.next != None:
                current = current.next
            return current.value

    def size(self):
        return self.items.size()