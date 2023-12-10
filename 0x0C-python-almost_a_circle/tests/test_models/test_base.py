#!/usr/bin/python3
"""define a test for the base model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """define test functions"""
    def test_init(self):
        """test object instantaion"""
        # test when init without parameter
        my_obj = Base()
        self.assertIsInstance(my_obj, Base)
        # test when init with an id value
        my_obj2 = Base(98)
        self.assertIsInstance(my_obj2, Base)
        self.assertAlmostEqual(my_obj2.id, 98)
        # test for an id of zero
        my_obj3 = Base(0)
        self.assertIsInstance(my_obj3, Base)
        # test for a negative id
        my_obj4 = Base(-2)
        self.assertIsInstance(my_obj4, Base)
        self.assertAlmostEqual(my_obj4.id, -2)

    def test_to_json_string(self):
        """tests to_json_string method"""
        # test with an empty list
        d_list = []
        my_obj = Rectangle(1, 1)
        self.assertAlmostEqual(my_obj.to_json_string(d_list), "[]")
        self.assertAlmostEqual(my_obj.to_json_string(None), "[]")
        # test with an actual list
        d_list = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertIsInstance(my_obj.to_json_string(d_list), str)

    def test_save_to_file(self):
        """test the save_to_file methon"""
        s = Square(3, 1, 1, 10)
        s2 = Square(4, 2, 2, 20)
        r1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file([s, s2])
        with open('Base.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([r1, r2])
        with open('Base.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 30)
        self.assertEqual(list_of_dicts[1]['x'], 4)

    def test_create(self):
        """testing the create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertAlmostEqual(r1.id, r2.id)
        self.assertAlmostEqual(r1.width, r2.width)
        self.assertAlmostEqual(r1.height, r2.height)
        self.assertAlmostEqual(r1.x, r2.x)
        self.assertAlmostEqual(r1.y, r2.y)

    def test_load_from_file(self):
        """testsing the load_from_file method"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertEqual(list_squares_input[0].id, list_squares_output[0].id)
