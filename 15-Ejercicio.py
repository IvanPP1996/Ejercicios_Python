#Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# * - La función recibirá dos String y retornará un Int.
# * - La diferencia en días será absoluta (no importa el orden de las fechas).
# * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

#Importación de librería datetime
from datetime import datetime

def fechas (fecha1, fecha2):
    if(len(fecha1) != 10) | (len(fecha2) != 10):
        return f'La fechas ingresadas no cumplen con el formato de ingreso indicado (dd/mm/yyyy).\nFecha 1 = ({fecha1}).\nFecha 2 = ({fecha2}).'
    else:
        fecha_conver_datetime_1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_conver_datetime_2 = datetime.strptime(fecha2, "%d/%m/%Y")
        dias_diferencia = (fecha_conver_datetime_2 - fecha_conver_datetime_1).days
        return f'La diferencia de días entre la fecha 1 ({fecha1}) y la fecha 2 ({fecha2}) es de: {abs(dias_diferencia)} días'

def ingreso_fechas ():
    fecha1 = input("Ingrese la primera fecha con este formato (dd/mm/yyyy): ")
    fecha2 = input("Ingrese la segunda fecha con este formato (dd/mm/yyyy): ")
    return fechas(fecha1, fecha2)

print(ingreso_fechas())
