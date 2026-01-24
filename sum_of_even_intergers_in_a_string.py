str1=input()
z=0
for i in range(len(str1)):
    if str1[i].isdigit() and int(str1[i])%2==0:
        z=z+int(str1[i])
print(z)