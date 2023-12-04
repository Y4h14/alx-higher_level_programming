#!/usr/bin/python3
"""define a fucntion that check class instances"""


def is_kind_of_class(obj, a_class):
    """
        check if an object is an instance of the class or a
        subclass of it
        Args:
            -obj: the object
            -a_class: the class
        Return:
            True if the object is an instance of or if the
            object is an instance of a class that inherited
            from the spesified class, otherwise false.
    """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
