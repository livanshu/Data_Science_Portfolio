



#!/bin/python3
#Author - Livanshu Kashyap

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    a = 0
    b = 0
    while a<len(c)-2:                   #loop until last 2 values are left
        a = a+1 if c[a+2] else a+2      #add 1 if c[a+2] is present else add 2
        b+=1                            #1 jump if added 2
    if a<len(c)-1:                      #last loop
        b+=1
    return b

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
