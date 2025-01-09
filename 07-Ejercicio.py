#* Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

frase = 'hola Hola bajo La mira de mira de HOla bajo BAJO'

frase = frase.upper().split()
diccionario_palabras_contadas = {}
contador = 0
for i in frase:
    for palabra in frase:
        if (i == palabra):
            contador += 1
    if i not in diccionario_palabras_contadas:
        diccionario_palabras_contadas[i] = contador
    contador = 0

for i, valor in diccionario_palabras_contadas.items():
    if (valor == 1):
        print(f'La palabra {i} esta {valor} vez repetida')
    else:
        print(f'La palabra {i} esta {valor} veces repetida')