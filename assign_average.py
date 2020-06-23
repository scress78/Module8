"""
Program: assign_average.py
Author:  Spencer Cress
Date: 06/22/2020

This is the py file for the Selection using dictionaries assignment
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
a_dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}


def assign_average(grade_percentage):
    """
    :param grade_percentage: Grade percentage to be converted into letter grade
    :returns: A letter grade based on a percentage
    :raises keyError: raises an exception
    """
    letter_grade = ''
    try:
        grade_percentage = float(grade_percentage)
    except ValueError:
        raise ValueError from None
    if 120 >= grade_percentage >= 90:
        letter_grade = 'A'
    elif 90 > grade_percentage >= 80:
        letter_grade = 'B'
    elif 80 > grade_percentage >= 70:
        letter_grade = 'C'
    elif 70 > grade_percentage >= 60:
        letter_grade = 'D'
    elif 60 > grade_percentage:
        letter_grade = 'F'
    else:
        letter_grade = 'Out of range 120-0... are we talking about the same test??'
    return letter_grade


def assign_gpa(a_letter_grade):
    gpa = 0.0
    a_dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    gpa = a_dict.get(a_letter_grade)
    return print(gpa)


if __name__ == '__main__':
    print(assign_average(100))
    assign_gpa(assign_average(80))
