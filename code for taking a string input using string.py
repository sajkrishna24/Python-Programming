# #  code for taking a string input using string(decimal no.) and convert all the digits in it, 
# to each of its respective place values and print the output as a string in the specified format
# 3472 to 3000 + 400 + 70 + 2
n=input()
n=" ".join(n)
L=n.split();l=len(L)
s=[]
for i in range(len(L)):
    if int(L[i])!=0:
        s.append(str(int(L[i])*(10**(l-i-1))))
print(" + ".join(s))