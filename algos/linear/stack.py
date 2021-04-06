from algos.linear.dynamic import DynamicArray

class Stack(DynamicArray):
    """The stack clas """
    def push(self,value):
        self.append(value)
    def pop(self,value):
        end_value = self.array[self.nums]
        self.remove(self.nums)
        return end_value

