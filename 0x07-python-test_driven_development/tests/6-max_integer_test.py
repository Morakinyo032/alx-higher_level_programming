#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def testResult(self):
        my_list = [-2, 4, -6, 12, 0, 5]
        list2 = []
        self.assertEqual(max_integer(my_list), 12)
        self.assertEqual(max_integer(list2), None)
