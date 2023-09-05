#!/usr/bin/python3
""" This is unittest for max intger function"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """ This is the test function"""

    def test_list(self):
        """test with a list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
