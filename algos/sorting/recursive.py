from algos.linear.dynamic import DynamicArray


def QuickSort(input_array):
    """This is an implementation of QuickSort"""
    if len(input_array) < 2:
        return input_array
    middle = len(input_array) // 2
    bigger = DynamicArray(input_array.gettype())
    smaller = DynamicArray(input_array.gettype())

    index = 0
    while index < len(input_array):
        if input_array[index] < input_array[middle]:
            smaller.append(input_array[index])
        if input_array[index] > input_array[middle]:
            bigger.append(input_array[index])

        index += 1
    element = DynamicArray(input_array.gettype())
    element.append(input_array[middle])
    element.extend(QuickSort(bigger))
    smaller = QuickSort(smaller)
    smaller.extend(element)
    return smaller
