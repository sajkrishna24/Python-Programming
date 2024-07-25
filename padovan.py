def padovan(n):
    if n<=0 or n==1 or n==2:
        return 1
    else:
        return padovan(n-2)+padovan(n-3)
num=int(input("enter the number=" ))
for i in range(num):
    print(padovan(i))
    
