#an encoded string "10110111011110 is decoded as "ABCD"
inpstr=input()
outstr="";cnt=0
for i in range(len(inpstr)):
    if inpstr[i] == "1":
        cnt+=1
    elif inpstr[i]=="0":
        outstr=outstr+chr(ord('A')+(cnt-1))
        cnt=0
    else:
        print("INVALID INPUT")
        exit()
print(outstr)