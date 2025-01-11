#Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada #palabra.
# * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def letra_mayuscula (palabra):
    palabra = palabra.split()
    palabra_mayuscula = []
    for contenido in palabra:
             palabra_mayuscula.append(contenido.capitalize())
             
    palabra_mayuscula = ' '.join(palabra_mayuscula)
    return palabra_mayuscula

def ingreso_palabra ():
    palabra = input('Ingrese un string: ')
    return letra_mayuscula(palabra)

print(ingreso_palabra())