#TO remove the all the vowels from the end of the given input string until a numeric constant occurs
#print the modified string and the count of removed vowels
#consider both uppercase and lowercase vowels
str1="A 1 E 2 i 3PU How Are You?"
outstr="";vowcnt=0
for i in range(len(str1)-1,-1,-1):
    if str1[i].isdigit():
            break
    if str1[i] in "AEIOUaeiou":
        vowcnt+=1
    else:
        outstr=str1[i]+outstr      
outstr=str1[0:i+1:1]+outstr
print(outstr)
print(vowcnt)