#!/bin/python3

import math
import os
import random
import re
import sys



def plusMinus(arr):
    p = m = z = 0
    n = len(arr)
    for item in arr:
        if item > 0:
            p += 1
        elif item < 0:
            m += 1
        else:
            z += 1

    print(round(p / n, 5))
    print(round(m / n, 5))
    print(round(z / n, 5))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
