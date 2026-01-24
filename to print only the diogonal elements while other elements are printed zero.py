#to print only the diogonal elements while other elements are printed zero
row =4;col=4
M=[[1,2,3,1],[4,3,2,1],[1,2,4,5],[4,3,2,6]]
for i in range(row):
    for j in range(col):
        if i<j or i>j:
            M[i][j]=0
        print(M[i][j],end="")
    print()