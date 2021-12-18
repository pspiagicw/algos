def heapify(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        right = largest
    if largest != i:
        heapify(self)


def insert(array, element):
    size = len(array)
    if size == 0:
        array.append(element)
    else:
        array.append(element)
        for i in range(len(array) // 2 - 1, -1, -1):
            heapify(array, len(array), i)


def delete(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(num)

    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)
