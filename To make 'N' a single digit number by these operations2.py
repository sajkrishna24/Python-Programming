#To make 'N' a single digit number by these operations
# if N is odd make floor(N/2)
# if N is even make floor((N-2)/2)
# if N is already a single digit print as it is
import math
n=int(input())
while(n>10):
    if n%2!=0:
        n=math.floor(n/2)
    else:
        n=math.floor((n-2)/2)
print(n)