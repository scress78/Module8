"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

Change this description to be more relevant.
This program creates a function that prints 'Hello World'
as output.  The function is then called.
"""


def in_set(a_set, an_element):
    """
    Use reST style.
    :param a_set: this is what the first parameter represents
    :param an_element: an element that might be in the set
    :returns: Boolean if the item is in a set
    """
    pass


if __name__ == '__main__':
    #call our functions
    hello_world()
    boolean_value_variable = True
    #store it as a variable since get_pi returns a value
    pi_value = get_pi(boolean_value_variable)
    #cast it as a string before printing!
    print("The value of pi is " + str(pi_value))



