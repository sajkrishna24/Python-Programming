#To show a input number in this form (eg:347 to 300+40+7)
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