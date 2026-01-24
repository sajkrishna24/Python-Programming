#last 10 digits in a string1
str1="987-af-6-gh-98743210,ppp,56789-rrr"
cnt=0;tmp=""
for i in range(len(str1)-1,-1,-1):
    if str1[i].isdigit():
        cnt+=1
        tmp=str1[i]+tmp
    if cnt==10:
        break
print(tmp)