#!/usr/bin/python3
"""defines a test class for the Rectangle model"""
from models.rectangle import Rectangle
import unittest
from io import StringIO
from unittest.mock import patch


class test_Rectangle(unittest.TestCase):
    """defines test functions for the rectangle model"""
    def test_init(self):
        """tests the initialization of a rectangle object"""
        # init with all parameters
        r1 = Rectangle(3, 5, 0, 0, 1)
        self.assertIsInstance(r1, Rectangle)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.width, 3)
        self.assertAlmostEqual(r1.height, 5)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)

        # init with minimal parameters
        r2 = Rectangle(3, 5)
        self.assertIsInstance(r2, Rectangle)
        self.assertAlmostEqual(r2.width, 3)
        self.assertAlmostEqual(r2.height, 5)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        # init with errorsome values

        with self.assertRaises(TypeError):
            Rectangle(2, 'x')
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_getter_setter(self):
        """tests the Rectangle getter and setter"""
        r1 = Rectangle(3, 5, 0, 0, 1)
        r1.id = 98
        r1.width = 7
        r1.height = 2
        r1.x = 1
        r1.y = 1
        self.assertAlmostEqual(r1.id, 98)
        self.assertAlmostEqual(r1.width, 7)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.x, 1)
        self.assertAlmostEqual(r1.y, 1)

    def test_area(self):
        """tests the area method"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(1800, 1400)

        self.assertAlmostEqual(r1.area(), 6)
        self.assertAlmostEqual(r2.area(), 2520000)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        """tests the display method"""
        r1 = Rectangle(2, 2)
        r1.display()
        r2 = Rectangle(2, 3, 2, 2)
        r2.display()
        self.assertEqual(mock_stdout.getvalue(),
                         "##\n##\n\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """test the string form of an object"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """testing the upload method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dectionary(self):
        """testing the to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()

        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
