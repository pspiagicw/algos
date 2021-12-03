import unittest
from algos.linear.dynamic import DynamicArray
from algos.errors.array_errors import IndexOutOfBoundsException,TypeException

class TestDynamicArray(unittest.TestCase):
    def test_appending(self):
        dynamic = DynamicArray(int)
        for i in range(5):
            dynamic.append(i)
        for i in range(5):
            self.assertEqual(i,dynamic[i])
    def test_removing(self):
        dynamic = DynamicArray(int)
        for i in range(5):
            dynamic.append(i)
        dynamic.remove(0)
        self.assertEqual(1,dynamic[0])
    def test_extending(self):
        array = DynamicArray(int)
        for i in range(30):
            array.append(i)
        other = DynamicArray(int)
        for i in range(30,40):
            other.append(i)
    def test_appending(self):
        dynamic = DynamicArray(str)
        for i in [ (i + 'ello') for  i in 'hjgls' ]:
            dynamic.append(i)
        for i , word in enumerate([ (i+'ello') for i in 'hjgls']):
            self.assertEqual(word,dynamic[i])
    def test_removing(self):
        dynamic = DynamicArray(str)
        for i in [ (i+'ello') for i in 'hjgls' ]:
            dynamic.append(i)
        dynamic.remove(0)
        self.assertEqual('jello',dynamic[0])
    def test_large_appending(self):
        dynamic = DynamicArray(int)
        for i in range(500):
            dynamic.append(i)
        for i in range(500):
            self.assertEqual(i,dynamic[i])

