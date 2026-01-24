#KADANE'S ALGORITHM
def kadane(L):
    csum=maxsum=L[0]
    for i in range(1,len(L)):
        csum=max(L[i],maxsum+L[i])
        maxsum=max(csum,maxsum)
    return maxsum