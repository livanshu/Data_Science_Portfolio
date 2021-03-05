#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sorted_arr = sorted(arr)    #used .sort() but error while executing because of "Nonetype"
    n = len(arr)
    minsum, maxsum = 0,0
    for i in range(n-1):
        minsum += sorted_arr[i]
    for i in range(1,n):
        maxsum += sorted_arr[i]
    print (minsum,maxsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
