#To find the second smallest number in an array using king and minister method with -infinity and +infinity
L=[int(x)for x in input().split()]
fs=float('inf');ss=float('inf')
for i in range(len(L)):
    if L[i]<fs:
        ss=fs
        fs=L[i]
    elif L[i]>fs and L[i]<ss:
        ss=L[i]
if ss!=float('inf'):
    print(ss)
else:
    print("SECOND SMALLEST VALUE IS NOT PRESENT")
     