#Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

def numero_armstrong (numero):
    total = 0
    for num in numero:
        num = int(num)
        total += num**(len(numero))
    if(numero != str(total)):
        return f'El número {numero} no es Armstrong ya que su suma de sus potencias por número es {total}'
    else:
        return f'El número {numero} es Armstrong ya que su suma de sus potencias por número es {total}'

def ingreso_numeros ():
    numero = input('Ingrese un número: ')
    return numero_armstrong(numero)

print(ingreso_numeros())