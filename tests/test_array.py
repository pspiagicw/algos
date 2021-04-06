import unittest

from algos.linear.array import Array
from algos.errors.array_errors import IndexOutOfBoundsException,TypeException
class TestArray(unittest.TestCase):
    def test_assignment_int(self):
        array = Array(5,int)
        for i in range(5):
            array.set(i,i)
        for i in range(5):
            self.assertEqual(i,array.get(i))
    def test_assignment_string(self):
        test_parameters = [ h + 'ello' for h in 'hgksd']
        array = Array(5,str)
        for i in range(5):
            array.set(i,test_parameters[i])
        for i in range(5):
            self.assertEqual(test_parameters[i],array.get(i))
    def test_assignment_float(self):
        test_parameters = [ 2.5 , 5.6 , 6.3 , 3.4 , 5.1 , 3.5 ]
        array = Array(len(test_parameters),float)
        array.set(0,4.56)
        for i in range(len(test_parameters)):
            array.set(i,test_parameters[i])
        for i in range(len(test_parameters)):
            self.assertEqual(array.get(i),test_parameters[i])
    def test_errors(self):
        array = Array(3,int)
        for i in range(4,10):
            with self.assertRaises(IndexOutOfBoundsException) as cm:
                array.get(i)
        with self.assertRaises(IndexOutOfBoundsException) as cm:
            array.get(-1)
        for i in [ 5.4 , 'hello' , {} , False ]:
            with self.assertRaises(TypeException) as cm:
                array.set(0,i)
    def test_type(self):
        array = Array(5,int)
        self.assertEqual(array.gettype(),int)
    def test_type_string(self):
        array = Array(5,str)
        self.assertEqual(array.gettype(),str)
    def test_type_float(self):
        array = Array(5,float)
        self.assertEqual(array.gettype(),float)
if __name__ == '__main__':
    unittest.main()
