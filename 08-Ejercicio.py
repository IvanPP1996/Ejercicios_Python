#Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

numero_decimal = 456
numero_binario = ''
while( numero_decimal > 0):
    numero = numero_decimal%2
    numero_binario = str(numero) + numero_binario
    numero_decimal = numero_decimal // 2

print(numero_binario)