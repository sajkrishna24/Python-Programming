#code for printing the series given below upto 'N' 1 2 4 8 16 . . . . N
n=int(input())
z=n;s=1
print(s,end=" ")
while(n!=0):
    s=s*2
    if (s>z):
        break
    print(s,end=" ")