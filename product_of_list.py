def list_product(s):
    product=1
    for num in s():
        product*=num
    return product

numb=[2,5,4,6]
product=list_product(numb)
print("Product of the list elements is:",product)