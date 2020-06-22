"""
Program: test_set_membership.py
Author:  Spencer Cress
Date: 06/22/2020

These are the tests for the set_membership program/ set assignment
"""
import unittest
from more_fun_with_collections.set_membership import in_set


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        """tests in_set for something that we know is in set"""
        first_set = set('abcdef')
        first_search = 'b'
        # create what we're looking for as a variable to pass into function
        self.assertTrue(in_set(first_set, first_search))

    def test_in_set_false(self):
        """tests in_set for something we know is not in the set"""
        another_set = 'abcdef'
        another_search = 'z'
        self.assertFalse(in_set(another_set, another_search))


if __name__ == '__main__':
    unittest.main()
