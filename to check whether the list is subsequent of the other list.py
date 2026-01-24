str1="MATHEW KURIEN"
str2="MWKR"
i=0;j=0
while i<len(str1) and j<len(str2):
    if str1[i]==str2[j]:
        i+=1;j+=1
    else:
        i+=1
if j==len(str2):
    print("Yes")
else:
    print("No")