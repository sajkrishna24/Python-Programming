#to check whether two given strings are anagram of each other or not
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
    dict1={};dict2={}
    for ele in m:
        if ele in dict1:
            dict1[ele]=dict1[ele]+1
        else:
            dict1[ele]=1
    for ele in n:
        if ele in dict2:
            dict2[ele]=dict2[ele]+1
        else:
            dict2[ele]=1
    if dict1==dict2:
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
