#Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
def factorial (numero):
    factorial = 1
    for num in range(1,numero+1):
        factorial *= num
    return f'El factorial de {numero} es {factorial}'

def ingreso_numero ():
    numero = int(input('Ingrese un número para hallar su factorial: '))
    return factorial(numero)

print(ingreso_numero())