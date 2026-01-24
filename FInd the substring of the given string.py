str1="ABCD"
for i in range(len(str1)):
    tmpstr=""
    for j in range(i,len(str1)):
        tmpstr=tmpstr+str1[j]
        print(tmpstr)