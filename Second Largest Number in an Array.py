# Second Largest Number in an Array
L=[30,20,10,10,50,40,100,25,100]
maxele=max(L)
maxcnt=L.count(maxele)
for i in range(maxcnt):
    L.remove(maxele)
print(max(L))