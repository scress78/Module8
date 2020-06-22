"""
Program: set_membership.py
Author:  Spencer Cress
Date: 06/22/2020

"""


def in_set(a_set, an_element):

    """
    Use reST style.
    :param a_set: a set to be fed into the function
    :param an_element: an element that might be in the set
    :returns: Boolean if the item is in a set
    """
    # my_boolean = False
    return an_element in a_set


my_set = set('jklmn')
my_search = 'k'
# print('k' in my_set)

if __name__ == '__main__':
    in_set(my_set, my_search)



