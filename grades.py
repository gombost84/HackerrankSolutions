import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for grade in grades:
        if grade <= 38:
            print(grade)
        elif (5 * math.ceil(grade / 5) - grade) >= 3:
            print(grade)
        else:
            print(5 * math.ceil(grade / 5))


stuff = [73, 67, 38, 33]


gradingStudents(stuff)