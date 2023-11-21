#!/usr/bin/python3
"""defines a class of linklist node"""


class Node:
    """defines a Node of a linked list"""
    def __init__(self, data, next_node=None):
        """
        Initilize the node instance
        Args:
            - data (int): the data of the node
            - nex_node (node): an object
        """
        if type(data) is int:
            self.__data = data
        else:
            raise TypeError('data must be an integer')

        if type(next_node) is Node or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """retuens the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data value"""

        if type(value) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """returns the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node value"""

        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """define a linked list"""

    def __init__(self) -> None:
        """intitialize the linked list instance"""
        self.__head = None

    def __str__(self):
        """print() representation for linked list object"""
        list = []
        temp = self.__head
        while temp is not None:
            list.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(list))

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
        Args:
            - value (int): value of the node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node
