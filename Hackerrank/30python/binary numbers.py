#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

a = str(bin(n))    #int to binary
a = a[2:]          #removing "0b" from bin(n)
maxi = 0
i,c = 0,0
while i<(len(a)):  #consecutive counter
    if a[i]=="1":
        c+=1
    else:
        c=0
    if c>maxi:
        maxi=c
    i +=1
print(maxi)
