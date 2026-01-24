#Smallest and Largest Number in an Array
L=[30,20,10,10,60,60,50,40]
mi=ma=L[0]
for i in range(1,len(L)):
    if (ma<L[i]):
        ma=L[i]
    if (mi>L[i]):
        mi=L[i]
print(mi,ma)