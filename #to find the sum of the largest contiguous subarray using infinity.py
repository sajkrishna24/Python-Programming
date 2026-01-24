#to find the sum of the contiguous subarray with 
#the largest sum within a one-dimensional 
#array of positive and negative numbers using infinity
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'MAXSUM_SUBARR' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY L as parameter.
#

def MAXSUM_SUBARR(L):
    # WRITE YOUR CODE HERE...
    gtr=float('-inf')
    for i in range(len(L)):
        for j in range(i,len(L)):
            s=sum(L[i:j+1])
            if s>gtr:
                gtr=s
    return gtr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    L_count = int(input().strip())

    L = list(map(int, input().rstrip().split()))

    maxsum = MAXSUM_SUBARR(L)

    fptr.write(str(maxsum) + '\n')

    fptr.close()
