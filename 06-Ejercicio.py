#Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

cadena = "Hola mundo"
cadena_al_reves = ""
for letra in range(len(cadena),0,-1):
    cadena_al_reves = cadena_al_reves + cadena[letra - 1]
print(cadena_al_reves)