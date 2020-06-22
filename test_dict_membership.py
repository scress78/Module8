"""
Program: test_dict_membership.py
Author:  Spencer Cress
Date: 06/22/2020

These are the tests for the set_membership program/ set assignment
"""
import unittest
from more_fun_with_collections.dict_membership import in_dict


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        """tests in_set for something that we know is in set"""
        first_dict = {'Apples': 90, 'Bananas': 100, 'Cherries': 300}
        first_search = 'Apples'
        # create what we're looking for as a variable to pass into function
        self.assertTrue(in_dict(first_dict, first_search))

    def test_in_dict_false(self):
        """tests in_set for something we know is not in the set"""
        second_dict = {'Apples': 90, 'Bananas': 100, 'Cherries': 300}
        second_search = 'Dogs'
        self.assertFalse(in_dict(second_dict, second_search))


if __name__ == '__main__':
    unittest.main()
