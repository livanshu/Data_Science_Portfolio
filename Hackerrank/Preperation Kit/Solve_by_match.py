#Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#Sample Input

#STDIN                       Function
#-----                       --------
#9                           n = 9
#10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()           #sorting the array elements (ascending)
    ar.append('*')      #Adding another value at end of list for index (i+1)
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:      #if current value is equal to next
            count = count+1     
            i+=2                #adding 2 to i and assigning result to i (paired)
        else:
            i+=1                #adding 1 to i and assigning result to i (non-paired)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()



