lst=[1,5,6,8,4,9,3,6]
counteven=0
countodd=0
for num in lst:
    if num%2 == 0:
        counteven+=1
    else:
       countodd+=1
print(f"no of even numbers are {counteven} and no of odd numbers are {countodd}")