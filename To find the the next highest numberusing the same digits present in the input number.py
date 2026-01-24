#To find the the next highest number using the same digits present in the input number
#4542 to 5244
#2187531 to 2311578
inpstr=input()
flag=0
L=list(inpstr)
for i in range(len(L)-2,-1,-1):
    if L[i]<L[i+1]:
        flag=1;break
if flag==1:
    for j in range(len(L)-1,i,-1):
        if L[i]<L[j]:
            break
    L[i],L[j]=L[j],L[i]
    L=L[:i+1]+sorted(L[i+1:])
    print("".join(L))
else:
    print("NOT POSSIBLE")
        
    
