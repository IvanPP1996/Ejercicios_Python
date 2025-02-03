#Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

from datetime import timedelta

def resul_milisegundos (dias, horas, minutos, segundos):
    total_mili = timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos).total_seconds() * 1000

    return f'''\nEl total de los dias, horas, minutos y segundos es de: {total_mili:.0f} milisegundos'''

def ingreso_datos ():
    dias = int(input('Ingrese el numero de dias: '))
    horas = int(input('Ingrese las horas: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))
    
    return resul_milisegundos(dias, horas, minutos, segundos)

print(ingreso_datos())