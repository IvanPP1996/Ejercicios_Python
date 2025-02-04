#Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.

def palabra_anagrama (palabra1, palabra2):
    #Se usa el método .lower() para convertir las palabras en minuscula
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if (palabra1 == palabra2):
        return False
    #Se usa la función sorted() para ordenar las palabras en orden alfabetico
    elif (sorted(palabra1) == sorted(palabra2)):
        return True
    else:
        return False

def ingreso_palabras ():
    palabra1 = input('Ingresa la palabra 1: ')
    palabra2 = input('Ingresa la palabra 2: ')
    return palabra_anagrama(palabra1, palabra2)

print (ingreso_palabras())