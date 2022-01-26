#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    minsum = sum(sorted(arr)[:-1])
    maxsum = sum(sorted(arr)[1:])
    print(minsum, maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
