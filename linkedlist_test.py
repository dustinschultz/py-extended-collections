import unittest
import extendedcollections

class TestLinkedList(unittest.TestCase):

        def test_add(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                self.assertTrue(str(l) == '1,2')

        def test_addFirst(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.addFirst(3)
                self.assertTrue(str(l) == '3,1,2')

        def test_addLast(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.addLast(3)
                self.assertTrue(str(l) == '1,2,3')

        def test_add_index(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.add(3,index=1)
                self.assertTrue(str(l) == '1,3,2')

        def test_size(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.add(3)
                self.assertTrue(l.size() == 3)
                self.assertTrue(len(l) == 3)

        def test_get(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.add(3)
                self.assertTrue(l.get(0) == 1)
                self.assertTrue(l.get(1) == 2)
                self.assertTrue(l.get(2) == 3)

        def test_getFirst(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.add(3)
                self.assertTrue(l.getFirst() == 1)

        def test_getLast(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                l.add(3)
                self.assertTrue(l.getLast() == 3)

        def test_contains(self):
                l = extendedcollections.LinkedList()
                l.add(1)
                l.add(2)
                self.assertTrue(1 in l)
                self.assertTrue(2 in l)
                self.assertFalse(3 in l)

if __name__ == "__main__":
        unittest.main()
