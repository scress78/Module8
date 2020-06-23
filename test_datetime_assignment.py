"""
Program: test_datetime_assignment.py
Author:  Spencer Cress
Date: 06/23/2020

Test for datetime assignment
"""
import unittest
import unittest.mock as mock
from more_fun_with_collections.datetime_assignment import half_birthday as hb


class MyTestCase(unittest.TestCase):

    def test_half_birthday(self):
        self.assertEqual(hb(2019, 8, 15), (2020, 2, 15))


if __name__ == '__main__':
    unittest.main()
