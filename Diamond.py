def diamond(num):
    #Upper part of the diamond
    for i in range(num):
        for j in range(num-i-1):
            print(" ",end="")
        for j in range(i*2+1):
            print("*",end="")
        print()
    #Lower part of the diamond
    for i in range(1,num):
        for j in range (i):
            print(" ",end="")
        for j in range((num-i)*2-1):
            print("*",end="")
        print()
diamond(5)
print("\n")