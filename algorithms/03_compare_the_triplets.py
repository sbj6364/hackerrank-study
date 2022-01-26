#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    point_a = 0
    point_b = 0

    for i in range(3):
        if a[i] > b[i]:
            point_a += 1
        elif a[i] < b[i]:
            point_b += 1

    return [point_a, point_b]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
