#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    apm = s[-2:]
    converted = []
    if apm == 'AM':
        converted_ms = s[2:-2]
        converted_h = s[:2]
        if int(converted_h) >= 12:
            converted_h = '00'
        converted = converted_h + converted_ms
    elif apm == 'PM':
        converted_ms = s[2:-2]
        converted_h = str(int(s[:2])+12)
        if int(converted_h) >= 24:
            converted_h = '12'
        converted = converted_h + converted_ms

    return converted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
