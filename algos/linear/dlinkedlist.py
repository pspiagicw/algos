class Node:
    def __init__(self,value,previous=None,next=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoubleLinkedList():
    def __init__(self):
        self.start = None
    def append(self,value):
        if not self.start:
            self.start = Node(value)
        else:
            node = self.start
            while node:
                if node.next == None:
                    node.next = Node(value)
                    break
                node = node.next
    def extend(self,other):
        if self.start == None:
            self.start = other.start
        else:
            node = self.start
            while node:
                if node.next == None:
                    node.next = other.start
                    break
                node = node.next
    def __len__(self):
        length = 0
        node = self.start
        while node:
            length += 1
            node = node.next
        return length
    def remove(self,value):
        node = self.start
        if node.value == value:
            self.start = None
        while node:
            if node.next.value == value:
                node.next = node.next.next
            node = node.next
    def __str__(self):
        string = ""
        node = self.start
        while node:
            string += str(node.value)
            node = node.next
            if node != None:
                string += "<-->"
        return string

