#Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# * Ejemplo: Ana lleva al oso la avellana.

def palindromo (palabra):
    palabra_sin_espacio = ''
    palabra = palabra.lower()
    for silaba in palabra:
        if(silaba != " "):
            palabra_sin_espacio += silaba
        else:
            continue
    if(palabra_sin_espacio == palabra_sin_espacio[::-1]):
        return f'La palabra o frase es un palíndromo'
    else:
        return f'La palabra o frase no es un palíndromo'

def ingreso_palabra ():
    palabra = input('Ingrese la palabra o frase: ')
    return palindromo(palabra)

print(ingreso_palabra())
