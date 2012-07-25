"""Extended Collections

Standard data structures implemented in python

Author: Dustin Schultz <schultz.dustin@gmail.com>

"""

class Node:
        """A individual node within a singly LinkedList"""
        def __init__(self):
                self.value = None
                self.next = None

class LinkedList:
        """A singly LinkedList data structure"""
        def __init__(self):
                """Create a new LinkedList."""
                self.__last = None
                self.__first = self.__last
                self.__size = 0

        def add(self,value,**kwargs):
                """Add a value to the end of the LinkedList

                Keyword arguments:
                index -- the index at which this value should be added.

                Raises:
                IndexError -- if index is out of bounds.
                """
                index = kwargs.get('index')
                if index:
                       self.__addIndex(value,index)
                else:
                       self.__add(value)
                self.__size += 1

        def addFirst(self,value):
                """Add a value to the first of the LinkedList."""
                new_node = Node()
                new_node.value = value
                new_node.next = self.__first
                self.__first = new_node

        def addLast(self,value):
                """Add a value to the last of the LinkedList."""
                self.add(value)

        def get(self,index):
                """Return the value at the given index.

                Raises:
                IndexError -- if index is out of bounds
                """
                if index > self.__size:
                        raise IndexError('Index '+str(index)+' out of bounds')
                ref = self.__first
                i = 0
                while ref.next is not None and i != index:
                        ref = ref.next
                        i = i+1
                return ref.value

        def getFirst(self):
                """Return the first value within the LinkedList."""
                return self.__first.value

        def getLast(self):
                """Return the last value within the LinkedList."""
                return self.__last.value

        def size(self):
                """Return the size of the LinkedList"""
                return self.__size

        def __add(self, value):
                """Private add function for adding a value."""
                new_node = Node()
                new_node.value = value
                if self.__first == None:
                        self.__first = new_node
                else:
                        self.__last.next = new_node
                self.__last = new_node

        def __addIndex(self, value, index):
                """Private add function with index for adding value."""
                if index == 0:
                        return self.addFirst(value)
                if index >= self.__size:
                        raise IndexError('Index '+str(index)+' out of bounds')
                ref = self.__first
                i = 0
                while ref.next is not None and i != index-1:
                        ref = ref.next
                        i+=1
                new_node = Node()
                new_node.next = ref.next
                new_node.value = value
                ref.next = new_node

        def __contains__(self, obj):
                """Return whether or not the object is in the LinkedList."""
                ref = self.__first
                while ref is not None:
                        if ref.value == obj:
                                return True
                        ref = ref.next
                return False

        def __len__(self):
                """Return the len() of the LinkedList."""
                return self.size()

        def __repr__(self):
                """Return a string representation of the LinkedList."""
                ref = self.__first
                s = []
                while ref is not None:
                        s.append(str(ref.value))
                        ref = ref.next
                return ",".join(s)
