#To check if the input strings can be derived from each other by circularly rotating them.
# The rotation can be clockwise or anti-clockwise
#Assume that there is no blank space inside the string.
str1=input()
str2=input();flag=0
if len(str1)!=len(str2):
    print("NO");exit()
for i in range(len(str1)):
    str2=str2[1:]+str2[:1]
    if str1==str2:
        flag=1;break
if flag==1:
    print("YES")
else:
    print("NO")