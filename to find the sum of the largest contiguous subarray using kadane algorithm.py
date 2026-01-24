#to find the sum of the contiguous subarray 
#with the largest sum within a one-dimensional array 
#of positive and negative numbers using kadane"s algorithm
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
    csum=maxsum=L[0]
    for i in range(1,len(L)):
        csum=max(L[i],csum+L[i])
        maxsum=max(csum,maxsum)
    return maxsum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    L_count = int(input().strip())

    L = list(map(int, input().rstrip().split()))

    maxsum = MAXSUM_SUBARR(L)

    fptr.write(str(maxsum) + '\n')

    fptr.close()
