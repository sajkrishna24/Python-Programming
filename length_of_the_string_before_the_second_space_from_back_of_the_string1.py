inpstr=input()
cnt=0;spcnt=0
for i in range(len(inpstr)-1,-1,-1):
    if inpstr[i]==" ":
        spcnt+=1
    elif spcnt==1:
        cnt+=1
    elif spcnt==2:
        break   
print(cnt)