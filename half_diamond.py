def half_diamond(num):
    #Upper part of the diamond
    for i in range(num):
        for j in range(i+1):
            print("*",end="")
        print()
    #Lower part of the diamond
    for i in range(num):
        for j in range((num-i)-1):
            print("*",end="")
        print()
half_diamond(5)
print("\n")