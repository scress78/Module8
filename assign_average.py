"""
Program: assign_average.py
Author:  Spencer Cress
Date: 06/22/2020


"""
"""average = 0
switch(average){
    case 'A': ...statements...
         break
    case B: ...statements...
         break
    case s: ...statements...
         break
    case e: ...statements...
         break
    default: ...statements...
        break
 }"""


def assign_average(grade_percentage):
    """
    :param grade_percentage: Grade percentage to be converted into letter grade
    :returns: A letter grade based on a percentage
    :raises keyError: raises an exception
    """
    try:
        grade_percentage = float(grade_percentage)
    except ValueError:
        raise ValueError from None
    pass


if __name__ == '__main__':
    assign_average("Taco")
