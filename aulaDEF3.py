def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(7, 9)
#Ou para utilizar o  Z 
soma(22, 77, 5)
 