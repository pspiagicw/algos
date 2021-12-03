from algos.linear.array import Array
from algos.errors.hash_errors import KeyNotFoundException

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.buckets = Array(50,Node)
    def add(self,key,value):
        i = self.hash(key)
        if self.buckets[i] == None:
            self.buckets[i] = Node(key,value)
        else:
            node = self.buckets[i]
            while node:
                if node.next == None:
                    node.next = Node(key,value)
                    break
                node = node.next
    def remove(self,key):
        i = self.hash(key)
        if self.buckets[i] == None:
            raise KeyNotFoundException(key)
        else:
            if self.buckets[i].key == key:
                if self.buckets[i].next == None:
                    self.buckets[i] = None
                else:
                    self.buckets[i] = self.buckets[i].next
            else:
                node = self.buckets[i]
                while node:
                    if node.next.key == key:
                        node.next = node.next.next
                    node = node.next
    def hash(self,key):
        index = sum(ord(i) for i in str(key))
        index *= len(key)
        index = index ^ 31
        index = index % 50
        return index
    def get(self,key):
        i = self.hash(key)
        if self.buckets[i] == None:
            raise KeyNotFoundException(key)
        else:
            if self.buckets[i].key == key:
                return self.buckets[i].value
            else:
                node = self.buckets[i]
                while node:
                    if node.key == key:
                        return node.value
                    node = node.next
