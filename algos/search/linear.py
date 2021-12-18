def LinearSearch(input_array, element):
    """This is the implementation of the simple Linear Search"""
    for i in range(len(input_array)):
        if i == element:
            return i
    return -1
