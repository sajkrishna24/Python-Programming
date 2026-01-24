# Second Largest Number in an Array using sort function
L=[30,20,10,10,50,40,100,25,100]
L=sorted(L);flag=0
for i in range(len(L)-1,0,-1):
    if L[i]!=L[i-1]:
        flag=1
        break
if flag==1:
    print("Second largest element is:",L[i-1])
else:
    print("Second largest element is not present")