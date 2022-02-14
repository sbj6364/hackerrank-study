#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max_score = min_score =  scores[0]
    max_cnt = min_cnt = 0
    for score in scores:
        # print(score)
        if score > max_score:
            # print('max break')
            max_score = score
            max_cnt += 1
        elif score < min_score:
            # print('min break')
            min_score = score
            min_cnt += 1
        else:
            continue
    return max_cnt, min_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

