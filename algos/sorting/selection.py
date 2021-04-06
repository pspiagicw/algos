
from algos.linear.array import Array
def SelectionSort(array:Array) -> Array:
    """This is the implementation of simple Selection Sort"""
    for i in range(len(array)):
        min_element = float('inf')
        min_index = 0
        for j in range(i,len(array)):
            if array[j] < min_element:
                min_element = array[j]
                min_index = j
        temp = array[min_index]
        array[min_index] = array[i]
        array[i] = temp
    return array

