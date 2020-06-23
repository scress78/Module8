"""
Program: datetime_assignment.py
Author:  Spencer Cress
Date: 06/23/2020

Datetime Assignment
"""
import datetime
from datetime import timedelta

#current = input("Input birthday in format YYYY-MM-DD")
#print(current.datetime())

#graduation_date = datetime.datetime(2020, 5, 17)
#print(graduation_date)


def half_birthday(birthyear, birthmonth, birthday):
    year = int(birthyear)
    month = int(birthmonth)
    day = int(birthday)
    birthday = datetime.datetime(year, month, day)
    #print(birthday)
    birthday_half = birthday + timedelta(days=182)
    #print(birthday_half)
    """
    Use reST style.

    :param birthyear: year of the birthday in YYYY format
    :param birthmonth: month of the birthday in MM format
    :param birthday: day of the birthday in DD format
    :returns: a date 6 months (182 days) after the date (birthday) entered
    representing a 'half birthday'
    """
    return str(birthday_half)


if __name__ == '__main__':
    half_birthday(2020, 8, 15)
