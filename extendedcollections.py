class Node:
        def __init__(self):
                self.value = None
                self.next = None

class LinkedList:
        def __init__(self):
                self.__last = None
                self.__first = self.__last
                self.__size = 0

        def add(self,value,**kwargs):
                index = kwargs.get('index')
                if index:
                       self.__addIndex(value,index)
                else:
                       self.__add(value)
                self.__size += 1

        def addFirst(self,value):
                new_node = Node()
                new_node.value = value
                new_node.next = self.__first
                self.__first = new_node

        def addLast(self,value):
                self.add(value)

        def get(self,index):
                if index > self.__size:
                        raise IndexError('Index '+str(index)+' out of bounds')
                ref = self.__first
                i = 0
                while ref.next is not None and i != index:
                        ref = ref.next
                        i = i+1
                return ref.value
        def getFirst(self):
                return self.__first.value

        def getLast(self):
                return self.__last.value

        def size(self):
                return self.__size

        def __add(self, value):
                new_node = Node()
                new_node.value = value
                if self.__first == None:
                        self.__first = new_node
                else:
                        self.__last.next = new_node
                self.__last = new_node

        def __addIndex(self, value, index):
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
                ref = self.__first
                while ref is not None:
                        if ref.value == obj:
                                return True
                        ref = ref.next
                return False

        def __len__(self):
                return self.size()

        def __repr__(self):
                ref = self.__first
                s = []
                while ref is not None:
                        s.append(str(ref.value))
                        ref = ref.next
                return ",".join(s)
