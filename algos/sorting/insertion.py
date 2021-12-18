def InsertionSort(array):
    """ This is the implementation of simple InsertionSort"""
    for i in range(len(array)):
        key = array[i]
        for j in range(len(array) - 2, -1, -1):
            if key < array[j]:
                array[j + 1] = array[j]
                array[j] = key
    return array
