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
        """Tests half_birthday function for accuracy"""
        self.assertEqual(hb(2019, 8, 15), '2020-02-13 00:00:00')


if __name__ == '__main__':
    unittest.main()
