#Given an array of integers and an integer target using dictionary
# write code for printing the absolute difference of the indices of two numbers 
# if the addition of those numbers is equal to target no.
#You may assume that each input have exactly one solution and you may not use the same element twice.
n=int(input())
L=[int(input())for i in range(n)]
tarno=int(input())
dict1={};flag=0
for i in range(n):
    diff=tarno-L[i]
    if diff in dict1:
        flag=1
        break
    else:
        dict1[L[i]]=i
if flag==1:
    print(abs(i-dict1[diff]))
else:
    print(-1)