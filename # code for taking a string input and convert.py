#  code for taking a string input(decimal no.) and convert all the digits in it, 
# to each of its respective place values and print the output as a string in the specified format
# 3472 to 3000 + 400 + 70 + 2
l=input()
n=int(l)
str1="";c=0
while n>0:
    a=n%10
    c+=1
    n=n//10
    if a!=0:
        str1=str1+" "+str(a*10**(c-1))
L=str1.split()
print(" + ".join(L[::-1]))