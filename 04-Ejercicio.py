#Escribe un programa que se encargue de comprobar si un número es o no primo.

##numero = int(input('Ingrese un número: '))
##incremento = 0
##for num in range(2,numero):
##    if(numero%num == 0):
##        incremento += 1
##
##if numero <= 0: print('Los números menores o iguales a 0 no son primos')
##elif incremento >= 1: print(f'El número {numero} no es primo')
##else: print(f'El número {numero} es primo')

# * Hecho esto, imprime los números primos entre 1 y 100.

for num in range(2,101):
    primo = True
    for i in range(2,num):
        if(num%i == 0):
            primo = False
            break
    if (primo == True):
        print(num)