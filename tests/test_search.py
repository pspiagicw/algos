from algos.search.linear import LinearSearch 
from algos.search.binary import BinarySearch 
from algos.linear.array import Array

import unittest
class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        array = Array(5 , int)
        for i in range(4 , -1 , -1):
            array[i] = 4 - i
        self.assertEqual(LinearSearch(array , 1) , 1)
        self.assertEqual(LinearSearch(array , 6) , -1)
    def test_binary_search(self):
        array = Array(5 , int)
        for i in range(4 , -1 , -1):
            array[i] = 4 - i
        self.assertEqual(BinarySearch(array , 1) , 1)
        self.assertEqual(BinarySearch(array , 6) , -1)
