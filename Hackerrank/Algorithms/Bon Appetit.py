#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    shared_cost = sum(bill)-bill[k]
    
    if ((shared_cost/2) == b):
        print ("Bon Appetit")
    else:
        print (int(b-(shared_cost/2)))
        

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
