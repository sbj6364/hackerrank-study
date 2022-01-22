#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    flag = 0
    
    if n % 2 == 1:
        flag = 1
    elif (2<=n) and (n<=5):
        flag = 0
    elif (6<=n) and (n<=20):
        flag = 1
    else:
        flag = 0
    
    if flag == 0:
        print("Not Weird")
    elif flag == 1:
        print("Weird")
