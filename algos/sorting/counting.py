from algos.arrays.array import Arrays


def CountingSort(array, limit):
    counter = {i: 0 for i in range(limit)}
    for i in array:
        counter[i] += 1
