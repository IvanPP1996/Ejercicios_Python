#Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono (figura):
    figura = figura.lower()
    if((figura=='triangulo') | (figura == 'rectangulo')):
        base = int(input('Ingrese la base de la figura: '))
        altura = int(input('Ingrese la altura de la figura: '))
        if(figura == 'triangulo'):
            area = (base * altura) / 2
            return f'El area del triangulo es de {area} metros cuadrados'
        elif(figura == 'rectangulo'):
            area = base * altura
            return f'El area del rectangulo es de {area} metros cuadrados'
    elif(figura == 'cuadrado'):
        lado = int(input('Ingrese el lado del cuadrado: '))
        if(figura == 'cuadrado'):
            area = lado * lado
            return f'{area} metros cuadrados'
    else:
        return 'No ingresaste niniguna de las figuras mencionadas'

def valores ():
    print('El siguiente programa permite saber el area de un cuadrado, triangulo o rectangulo. \nSolo permite estas tres figuras por tal motivo si ingresas otra figura no permitira dar el resultado del area.\n')
    figura = input("ingresa alguna de las tres figuras para conocer su area: ")
    return area_poligono(figura)

print(valores())