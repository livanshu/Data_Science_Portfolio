#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    a = 0
    b = 0
    maxi = scores[0]
    mini = scores[0]
    for i in range(len(scores)):
        if (scores[i])< mini:
            mini = scores[i]    #this line to counter the ou of index error
            a += 1
        if (scores[i])>maxi:
            maxi = scores[i]
            b += 1
    return b,a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
