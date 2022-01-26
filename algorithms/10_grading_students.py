#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    final = []
    rounded = 0
    for grade in grades:
        plus = grade % 5
        if grade < 38:
            rounded = grade
        elif plus > 2:
            rounded = grade + 5 - plus
        else:
            rounded = grade
        final.append(rounded)
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
