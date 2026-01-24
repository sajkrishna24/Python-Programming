#to display the 2d array in the form of matrix 
#and to find the sum of the elements in aa matrix
row=5;col=4
M=[[1,3,2,1],[4,3,2,1],[1,2,3,4],[4,3,2,6],[1,2,7,9]]
s=0;t=0
for i in range(row):
    print(*M[i])
    s=sum(M[i])
    t=t+s
print(t)