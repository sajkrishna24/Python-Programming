#To make 'N' a single digit number by these operations
# if N is odd make floor(N/2)
# if N is even make floor((N-2)/2)
# if N is already a single digit print as it is  
import math
n=int(input())
if n%10==n:
    print(n)
elif n%2==0:
    s=math.floor((n-2)/2)
    if s%10==s:
        print(s)
    elif s%2==0:
        s=math.floor((s-2)/2)
        print(s)
    else:
        s=math.floor(s/2)
        print(s)
else:
    s=math.floor(n/2)
    if s%10==s:
        print(s)
    elif s%2==0:
        s=math.floor((s-2)/2)
        print(s)
    else:
        s=math.floor(s/2)
        print(s)