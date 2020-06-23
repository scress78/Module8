"""
Program: test_assign_average.py
Author:  Spencer Cress
Date: 06/22/2020

Tests assign_average functions
"""
import unittest
import unittest.mock as mock
from more_fun_with_collections.assign_average import assign_average as aa


class MyTestCase(unittest.TestCase):

    def test_assert_average_A(self):
        self.assertEqual(aa(100), 'A')

    def test_assert_average_B(self):
        self.assertEqual(aa(85), 'B')

    def test_assert_average_C(self):
        self.assertEqual(aa(71), 'C')

    def test_assert_average_D(self):
        self.assertEqual(aa(64), 'D')

    def test_assert_average_F(self):
        self.assertEqual(aa(13), 'F')

    def test_assert_average_Invalid(self):
        with self.assertRaises(ValueError):
            aa("Taco")




if __name__ == '__main__':
    unittest.main()
