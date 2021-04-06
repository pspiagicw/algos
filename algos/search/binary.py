from algos.linear.dynamic import DynamicArray

def BinarySearch(input_array,element):
    """ The implementation of Binary Search"""
    high = len(input_array)
    low = 0
    while low < high:
        middle = ( high + low ) // 2
        if input_array[middle] == element:
            return middle
        if element < input_array[middle]:
            high = middle - 1
        if element > input_array[middle]:
            low = middle + 1
    return -1
