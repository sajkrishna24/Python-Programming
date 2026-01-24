#Given an array of integers and finding an integer target, 
# write code for printing the absolute difference of the indices of two numbers 
# if the addition of those numbers is equal to target no.
#You may assume that each input have exactly one solution and you may not use the same element twice.
n=int(input())
L=[int(input())for i in range(n)]
tarno=int(input())
for i in range(n):
    for j in range(i+1,n):
        if L[i]+L[j]==tarno:
            print(abs(i-j))
            exit()
print("-1")