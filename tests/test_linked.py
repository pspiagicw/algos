from algos.linear.linkedlist import LinkedList



import unittest
class TestLinkedList(unittest.TestCase):
    def test_linked(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(2)
        linkedlist.append(3)
        self.assertEqual("1-->2-->3",linkedlist.__str__())
        self.assertEqual(3,len(linkedlist))

