
from algos.linear.array import Array
from algos.sorting.selection import SelectionSort

import unittest
class TestSelectionSort(unittest.TestCase):
    def test_sort(self):
        array = Array(5,int)
        for i in range(4,-1,-1):
            array[i] = 4-i
        correct_array = Array(5,int)
        for i in range(5):
            correct_array[i] = i
        sorted_array = SelectionSort(array)
        self.assertEqual(sorted_array.to_array() , correct_array.to_array())
