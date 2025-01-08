#Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#Definimos el range con dos valores el primero desde donde inicia y el ultimo hasta donde debe terminar en este caso se pone 101 pero llega hasta 100
for numero in range(1,101):
    if(numero%3 == 0 & numero%5 == 0):
        print('fizzbuzz')
    elif(numero%3 == 0):
        print('fizz')
    elif(numero%5 == 0):
        print('buzz')
    else:
        print(numero)