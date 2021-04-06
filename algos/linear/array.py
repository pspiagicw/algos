
import random

from algos.errors.array_errors import TypeException
from algos.errors.array_errors import IndexOutOfBoundsException
class Array:
    """The main Array Class providing arrays for the module"""
    def __init__(self,length,array_type):
        self.length = length
        self.max_index = length-1
        self.array = [ random.randint(3,100) for _ in range(length) ]
        self.array_type = array_type
    def get(self,index:int) -> 'Array Type':
        if index > self.max_index:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        return self.array[index]
    def set(self,index:int,value) -> None:
        if type(value) != self.array_type:
            raise TypeException(self.array_type,type(value))
        if index > self.max_index:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        self.array[index] = value
    def __getitem__(self,index:int) -> 'Array Type':
        return self.get(index)
    def __setitem__(self,index:int,value) -> None:
        self.set(index,value)
    def __str__(self):
        for i in self.array:
            print(i,end=' ')
        print()
    def to_array(self):
        return self.array
    def __len__(self):
        return self.length
    def gettype(self):
        return self.array_type


