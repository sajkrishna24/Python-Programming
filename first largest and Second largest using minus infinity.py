#first largest and Second largest using minus infinity(by king and minister method)
L=[30,20,10,10,50,40,100,25,100]
flar=float('-inf');slar=float('-inf')
for i in range(len(L)):
    if L[i]>flar:
        slar=flar
        flar=L[i]
    elif L[i]<flar and L[i]>slar:
        slar=L[i]
print("Second largest element is:",slar)