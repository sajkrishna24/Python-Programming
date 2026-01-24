#To check whether the input string is palindrome
str1=input().lower()
if str1==str1[::-1]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")