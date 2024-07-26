def rhombus_star_pattern(n):
    for i in range(n):
        print(' '*(n-i-1)+'* '*n)
rhombus_star_pattern(4)
print("\n")

def mirror_rhombus_star_pattern(n):
    for i in range(n):
        print(' ' * i+'* ' * n)
mirror_rhombus_star_pattern(4)
print("\n")