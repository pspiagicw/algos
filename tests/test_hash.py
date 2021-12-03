from algos.hash.simple import HashTable


import unittest

class TestHash(unittest.TestCase):
    def test_hash(self):
        hashmap = HashTable()
        hashmap.add('hello','gello')
        hashmap.add('gello','hello')
        self.assertEqual(hashmap.get('hello'),'gello')
        self.assertEqual(hashmap.get('gello'),'hello')

