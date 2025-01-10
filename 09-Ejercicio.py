#Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre 
#letras o símbolos y dos espacios entre palabras " ".

texto = 'Hola a'
texto_a_morse = ''
alfabeto_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}
texto = texto.upper()
for letra in texto:
    for llave, valor in alfabeto_morse.items():
        if (letra == llave):
            texto_a_morse = texto_a_morse + valor
print(texto_a_morse)
