from linkedlist import LinkedList
from linkedlist.node import LinkedListNode  


class Queue:

    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items.size() == 0:
            return None
        else:
            return self.items.remove(self.items.head.value).value

    def front(self):
        if self.items.size() == 0:
            return None
        else:
            return self.items.head.value

    def rear(self):
        if self.items.size() == 0:
            return None
        else:
            current = self.items.head
            while current.next != None:
                current = current.next
            return current.value

    def size(self):
        return self.items.size()
