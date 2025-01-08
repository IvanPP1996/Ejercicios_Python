#Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# * - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores. 0, 1, 1, 2, 3, 5, 8, 13...
numero1 = 0
numero2 = 1
print(numero1)
print(numero2)
for numero in range(49):
    resultado = numero1 + numero2
    print(resultado)
    numero1 = numero2
    numero2 = resultado
