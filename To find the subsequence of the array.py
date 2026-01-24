#to find the subsequence of the array
L="ABCD"
for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            for l in range(len(L)):
                if i!=j and i!=k and j!=k and j!=l and k!=l and l!=i:
                    print(L[i],L[j],L[k],L[l])