"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

Change this description to be more relevant.
This program creates a function that prints 'Hello World'
as output.  The function is then called.
"""


def in_dict(a_dict, a_key):
    """Use reST style.
    :param a_dict: a dictionary to be entered into the function
    :param a_key: a key item to search for in the dictionary
    :returns: True if item key is in the dictionary and false if not
    """
    return a_key in a_dict


first_dict = {'Apples': 90, 'Bananas': 100, 'Cherries': 300}
first_search = 'Apples'
# print(first_search in first_dict)

if __name__ == '__main__':
    in_dict(first_dict, first_search)
