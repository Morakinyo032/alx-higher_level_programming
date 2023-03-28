#!/usr/bin/python3

"""Module 100-singly_linked_list"""


class Node:
    """Class node of singly linked list.


    """

    def __init__(self, data, next_node=None):
        """Constructor.

        Args:
            data: First parameter
            next_node: Second parameter

        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter to retrieve self.__data.

        Raises:
            TypeError: If data is not an integer.

        Returns: self.__data.

        """

        return(self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter to retrieve self.__next_node.

        Raise:
            TypeError: If next_node is not of type Node.

        """

        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """

    """

    __head = None
    def __init__(self):
        """
        Simple constructor.
        """

        pass

    def __str__(self):
        l = []
        ptr = self.__head
        while ptr is not None:
            l.append(str(ptr.data))
            ptr = ptr.next_node
        return("\n".join(l))

    def sorted_insert(self, value):
        """Inserts a new Node into the correct position in the list.

        Args:
            value: Value of the Node data.

        """

        new_node = Node(value)
        ptr = self.__head
        if self.__head is None:
            self.__head = new_node
            return(self.__head)
        while ptr is not None:
            ptr1 = ptr.next_node
            if ptr1 is not None:
                if new_node.data > ptr.data:
                    if new_node.data <= ptr1.data:
                        new_node.next_node = ptr1
                        ptr.next_node = new_node
                        return(self.__head)
                else:
                    new_node.next_node = ptr
                    self.__head = new_node
                    return(self.__head)
            else:
                if new_node.data > ptr.data:
                    ptr.next_node = new_node
                    return(self.__head)
            ptr = ptr.next_node
