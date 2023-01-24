def multiply(*args):
    total = 0 
    for numero in args:
        total *= numero
    return total 

mult = multiply(1,2,3,4,5)
print(mult)


