#!/usr/bin/python3
"""defines a test class for the Square model"""
from models.square import Square
import unittest
from io import StringIO
from unittest.mock import patch


class test_Square(unittest.TestCase):
    """defines test functions for the Square model"""
    def test_init(self):
        """tests the initialization of a Square object"""
        # init with all parameters
        r1 = Square(3, 0, 0, 1)
        self.assertIsInstance(r1, Square)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.size, 3)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)

        # init with minimal parameters
        r2 = Square(3)
        self.assertIsInstance(r2, Square)
        self.assertAlmostEqual(r2.size, 3)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        # init with errorsome values

        with self.assertRaises(TypeError):
            Square(2, 'x')
        with self.assertRaises(ValueError):
            Square(10, -2, 3, -1)

    def test_getter_setter(self):
        """tests the Square getter and setter"""
        r1 = Square(3, 0, 0, 1)
        r1.id = 98
        r1.size = 7
        r1.x = 1
        r1.y = 1
        self.assertAlmostEqual(r1.id, 98)
        self.assertAlmostEqual(r1.size, 7)
        self.assertAlmostEqual(r1.x, 1)
        self.assertAlmostEqual(r1.y, 1)

    def test_area(self):
        """tests the area method"""
        r1 = Square(3, 3)
        r2 = Square(1800)

        self.assertAlmostEqual(r1.area(), 9)
        self.assertAlmostEqual(r2.area(), 3240000)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        """tests the display method"""
        r1 = Square(2)
        r1.display()
        r2 = Square(2, 2, 2)
        r2.display()
        self.assertEqual(mock_stdout.getvalue(),
                         "##\n##\n\n\n  ##\n  ##\n")

    def test_str(self):
        """test the string form of an object"""
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")

    def test_update(self):
        """testing the upload method"""
        r1 = Square(10, 10, 10, 1)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
        r1.update(89, 2, 1, 2)
        self.assertEqual(str(r1), "[Square] (89) 1/2 - 2")
        r1.update(x=1, y=3, size=4)
        self.assertEqual(str(r1), "[Square] (89) 1/3 - 4")

    def test_to_dectionary(self):
        """testing the to_dictionary method"""
        r1 = Square(10, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()

        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'size': 10})
