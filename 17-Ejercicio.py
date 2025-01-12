#Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
# * - La función recibirá dos parámetros:
# * - Un array que sólo puede contener String con las palabras "run" o "jump"
# * - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# * - La función imprimirá cómo ha finalizado la carrera:
# * - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
# * - Si hace "jump" en "_" (suelo), se variará la pista por "x".
# * - Si hace "run" en "|" (valla), se variará la pista por "/".
# * - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def carrera (corre_salto, pista):
    for i in range(0, len(pista)):
        if ((corre_salto[i]=='run') & (pista[i]=='|')):
            pista = pista[:i] + pista[i:].replace('|','/',1)
        elif((corre_salto[i]=='jump') & (pista[i]=='_')):
            pista = pista[:i] + pista[i:].replace('_','X',1)
    for i in pista:
        if((i=='X') | (i=='/')):
            return f'{False} No ha superado la carrera.\nEl trayecto de pista que hizo fue {pista}.\nLas acciones que realizo fueron las siguientes {corre_salto}.'
    return f'{True} Ha superado la pista.\nEl trayecto de pista que hizo fue {pista}.\nLas acciones que realizo fueron las siguientes {corre_salto}.'

def ingreso_datos ():
    pista = input('Ingrese el trayecto de la pista recordando que:\n("_") = Suelo.\n("|") = Valla.\nIngrese el trayecto: ')
    corre_salto = []
    for accion in range(len(pista)):
        corre_salto.append(input('Ingrese "run" para correr o "jump" para saltar las vallas de la pista: '))
    return carrera(corre_salto, pista)

print(ingreso_datos())