str1="ZABCZZZDEFZ"
L=list(str1)
print(L)
for i in range(len(str1)):
    if(L[i]=='Z'):
        L[i]='#'
print(L)
str1="".join(L)
print(str1)