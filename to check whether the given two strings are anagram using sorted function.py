#to check whether the given two strings are anagram using sorted function
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ANAGRAM' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING m
#  2. STRING n
#

def ANAGRAM(m, n):
    # WRITE YOUR CODE HERE...
    a=sorted(m)
    b=sorted(n)
    if a==b:
        return "YES"
    else:
        return"NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = input()

    n = input()

    z = ANAGRAM(m, n)

    fptr.write(z + '\n')

    fptr.close()
