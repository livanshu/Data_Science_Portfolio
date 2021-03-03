#An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. 
#Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:
#A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
#Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

#Sample Input

#8
#UDDDUDUU

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0                   
    valley = 0
    for i in range(steps):
        if (path[i]=='U'):          #To check if next path is up or down
            level += 1              # +1 level if up
            if (level==0):
                valley += 1         # +1 valley if 0
        else:
            level -=1               # -1 level if down
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
