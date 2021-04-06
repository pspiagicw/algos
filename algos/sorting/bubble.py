def BubbleSort(input_array):
    """This is the implementation of BubbleSort"""
    for i in range(len(input_array)):
        for j in range(len(input_array) - i):
            if input_array[j] > input_array[j+1]:
                input_array[j+1] , input_array[j] = input_array[j] , input_array[j+1]
        return input_array

