from algos.linear.array import Array
from algos.errors.array_errors import IndexOutOfBoundsException, TypeException
from algos.search.linear import LinearSearch


class DynamicArray:
    def __init__(self, input_type):
        self.array = Array(10, input_type)
        self.array_type = input_type
        self.nums = 0
        self.max_index = 9

    def __getitem__(self, index):
        if index > self.nums:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutofboundsException(index)
        return self.array[index]

    def __setitem__(self, index, value):
        if index > self.nums:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        self.array[inde] = value

    def append(self, value):
        if (self.nums / self.max_index) > 0.7:
            self.new_array = Array((self.max_index + 1) * 2, self.array_type)
            for i in range(self.nums):
                self.new_array[i] = self.array[i]
            self.max_index = self.max_index * 2
            self.array = self.new_array
            self.array[self.nums] = value
            self.nums += 1
        else:
            self.array[self.nums] = value
            self.nums += 1

    def remove(self, index):
        if index > self.nums:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        self.new_array = Array(self.max_index + 1, self.array_type)
        for i in range(index):
            self.new_array[i] = self.array[i]
        for i in range(index + 1, self.nums, 1):
            self.new_array[i - 1] = self.array[i]
        self.array = self.new_array
        self.nums -= 1

    def get(self, index: int) -> 'Array Type':
        if index > self.nums:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        return self.array[index]

    def set(self, index: int, value) -> None:
        if type(value) != self.array_type:
            raise TypeException(self.array_type, type(value))
        if index > self.nums:
            raise IndexOutOfBoundsException(index)
        if index < 0:
            raise IndexOutOfBoundsException(index)
        self.array[index] = value

    def __len__(self):
        return self.nums

    def extend(self, other_array):
        for i in range(len(other_array)):
            self.append(other_array[i])

    def gettype(self):
        return self.array_type

    def index(self):
        index = LinearSearch(self.array)
        if index > self.nums:
            return -1
        return index

    def to_array(self):
        array = list()
        for i in range(self.nums):
            array.append(self.array[i])
        return array

    def __str__(self):
        string = ""
        for i in range(self.nums):
            string += str(array[i])
            string += " "
        return string
