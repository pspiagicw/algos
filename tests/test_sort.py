from algos.linear.array import Array
from algos.sorting.bubble import BubbleSort
from algos.sorting.insertion import InsertionSort
from algos.sorting.selection import SelectionSort
from algos.sorting.recursive import QuickSort
import unittest


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        array = Array(5,int)
        for i in range(4,-1,-1):
            array[i] = 4-i
        correct_array = Array(5,int)
        for i in range(5):
            correct_array[i] = i
        sorted_array = BubbleSort(array)
        self.assertEqual(sorted_array.to_array() , correct_array.to_array())

    def test_insertion_sort(self):
        array = Array(5,int)
        for i in range(4,-1,-1):
            array[i] = 4-i
        correct_array = Array(5,int)
        for i in range(5):
            correct_array[i] = i
        sorted_array = InsertionSort(array)
        self.assertEqual(sorted_array.to_array() , correct_array.to_array())

    def test_selection_sort(self):
        array = Array(5,int)
        for i in range(4,-1,-1):
            array[i] = 4-i
        correct_array = Array(5,int)
        for i in range(5):
            correct_array[i] = i
        sorted_array = SelectionSort(array)
        self.assertEqual(sorted_array.to_array() , correct_array.to_array())

    def test_quick_sort(self):
        array = Array(5,int)
        for i in range(4,-1,-1):
            array[i] = 4-i
        correct_array = Array(5,int)
        for i in range(5):
            correct_array[i] = i
        sorted_array = QuickSort(array)
        self.assertEqual(sorted_array.to_array() , correct_array.to_array())
