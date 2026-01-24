L=[10,20,30,40,50,60,70,80,90]
i=0;j=len(L)-1
while(i<j):
    print(L[i],L[j])
    i+=1
    j-=1
if i==j:
    print(L[i],"#")