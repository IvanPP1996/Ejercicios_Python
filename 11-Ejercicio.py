#Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
def cadenas (str1, str2):
    out1 = ''
    out2 = ''
    for caracter1 in str1:
        out1 += caracter1
    for caracter2 in str2:
        if(caracter2 == ' '):
            out2 += ' '
        elif caracter2 not in str1:
            out2 += caracter2
    return f'El string de salida 1 es "{out1}" y el string de salida 2 es "{out2}"'

def ingreso_strings ():
    str1 = input('Ingrese el primer string o cadena de caracteres: ')
    str2 = input('Ingrese el segundo string o cadena de caracteres: ')
    return cadenas(str1, str2)

print(ingreso_strings())