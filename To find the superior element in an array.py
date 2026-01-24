#to find the superior element in an array
#superior element is one which is greater than all the elements in its right side
#the rightmost element istelf is the superior element
def Find_Number_of_superior_elements(L,n):
    cnt=0
    m=float('-inf')
    for i in range(n-1,0,-1):
        if L[i]>m:
            cnt+=1
            m=L[i]
    return cnt
l=[8,10,6,2,9,7]
r=6
Find_Number_of_superior_elements(l,r)