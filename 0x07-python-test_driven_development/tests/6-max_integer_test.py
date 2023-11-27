#!/usr/bin/python3
"""Test the max ingter function"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    def test_positvie_int(self):
        #test max with positive integers
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_Negative_int(self):
        #testing max with negative int
        self.assertAlmostEqual(max_integer([10, 2, -12, 12, 1]), 12)

    def test_empty_list(self):
        #testing for worng values
        self.assertAlmostEqual(max_integer([]), None)
