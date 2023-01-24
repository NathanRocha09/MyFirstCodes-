"""
args - Argumentos não nomeados 
*args (empacotamento e desempacotamento)desempacotamento

""" 

x,y, *resto = 1,2,3,4
print(x,y, resto)


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total 

soma_1 = soma(1,2,3)
print(soma_1)

soma_4 = soma(4,5,6)
print(soma_4)

numeros = 1,2,3,4,5,6,7,8,33,77

outra_soma = soma(*numeros)
print(outra_soma)



