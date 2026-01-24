#To remove the vowels from the end of the given input string until a numeric constant occurs 
str1="a 1 e 2 0 3iU How Are You?"
outstr=""
for i in range(len(str1)-1,-1,-1):
    if str1[i] not in "AEIOUaeiou":
        outstr=str1[i]+outstr
        if str1.isdigit():
            break
outstr=str1[i::-1]+outstr
print(outstr)

