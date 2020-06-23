"""
Program: datetime_assignment.py
Author:  Spencer Cress
Date: 06/23/2020

Datetime Assignment
"""
from datetime import datetime, timedelta

#current = input("Input birthday in format YYYY-MM-DD")
#print(current.datetime())

graduation_date = datetime.datetime(2020, 5, 17)
print(graduation_date)


def half_birthday(birthyear, birthmonth, birthday):
    year = int(birthyear)
    month = int(birthmonth)
    day = int(birthday)
    birthday = datetime.(year, month, day)
    print(birthday)
    #birthday_half = birthday + timedelta(days=182)
    #print(birthday_half)
    """
    Use reST style.

    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    pass


if __name__ == '__main__':
   #half_birthday(2020, 5, 17)
