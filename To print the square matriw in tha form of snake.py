#To print the square matriw in tha form of snake
n=int(input());t=2
for i in range(n):
    if i%2==0:
        for j in range(n):
            print((i*n)+(j+1),end=" ")
    else:
        for j in range(n):
            print((t*n)-j,end=" ")
        t+=2
    print()