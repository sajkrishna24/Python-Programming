#To move the zeroes to the side and append the average of the non-zero numbers in the array
L=[10,0,20,0,30]
cnt=L.count(0)
for i in range(cnt):
    L.remove(0)
avg=sum(L)//len(L)
for i in range(cnt):
    L.append(0)
L.append(avg)
print(*L)