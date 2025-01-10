#Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }

expresion = '{ [ a * ( c + d ) ] - 5 }'
expresion = '{ a * ( c + d ) ] - 5 }'
corchetes = {
    '}' : '{',
    ']' : '[',
    ')' : '('
}
lista_corchetes = []
for dato in expresion:
    if (dato in corchetes.values()):
        lista_corchetes.append(dato)
    elif(dato in corchetes.keys()):
        if lista_corchetes and lista_corchetes[-1] == corchetes[dato]:
            lista_corchetes.pop()
        else:
            lista_corchetes.append(dato)
            break

if(len(lista_corchetes) == 0):
    print('La expresion esta balanceada')
else:
    print('La expresion no esta balanceada')