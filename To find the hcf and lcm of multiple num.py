#To find the hcf and lcm of multiple numbers
def find_gcd(m,n):
    while(n):
        rem=m%n
        m=n
        n=rem
    return m
def find_lcm(m,n):
    return m*n//find_gcd(m,n)

n=int(input())
L=[int(x)for x in input().split()]
gcd=find_gcd(L[0],L[1])
lcm=find_lcm(L[0],L[1])
for i in range(2,len(L)):
    gcd=find_gcd(gcd,L[i])
    lcm=find_lcm(lcm,L[i])
print(f"HCF={gcd} LCM={lcm}")