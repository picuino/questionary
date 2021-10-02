import re


def primera_franja(valor):
    return int(str(valor)[0])

def segunda_franja(valor):
    return int(str(valor*10)[1])

def multiplicador(valor):
    if valor < 10:
        return -1
    if valor < 100:
        return 0
    if valor < 1000:
        return 1
    if valor < 10000:
        return 2
    if valor < 100000:
        return 3
    if valor < 1000000:
        return 4
    if valor < 10000000:
        return 5
    return 6


def valor_tostring(valor):
    if valor<10:
        return str(round(valor, 1))    
    if valor<1000:
        return str(int(round(valor, 0)))
    if valor<10000:
        return str(round(valor/1000, 1)) + 'k'
    if valor<100000:
        return str(int(round(valor/1000, 0))) + 'k'
    if valor<1000000:
        return str(int(round(valor/1000, 0))) + 'k'
    if valor<10000000:
        return str(round(valor/1000000, 1)) + 'M'
    return str(int(round(valor/1000000, 0))) + 'M'

    
text = """
- Title: Código de colores %s Ohmios
  Question: ¿Qué colores tendrá una resistencia de %sΩ?
  Choices:
    - %s
    - %s
    - %s
    - %s
"""

def get_colores(primera, segunda, multip):
    colores =['Negro', 'Marrón', 'Rojo', 'Naranja', 'Amarillo',
              'Verde', 'Azul', 'Violeta', 'Gris', 'Blanco', 'Oro']
    if primera < 0:
        primera = 9
    if primera > 9:
        primera = 0
    if segunda < 0:
        segunda = 9
    if segunda > 9:
        segunda = 0
    return colores[primera]+ ', ' + colores[segunda] + ', ' + colores[multip] + ', Oro'

    
def main():
    valores = [ 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2 ]
    valores = valores + \
       [int(val*10+0.5) for val in valores] + \
       [int(val*100+0.5) for val in valores] + \
       [int(val*1000+0.5) for val in valores] + \
       [int(val*10000+0.5) for val in valores] + \
       [int(val*100000+0.5) for val in valores] + \
       [int(val*1000000+0.5) for val in valores]

    for valor in valores:
        primera = primera_franja(valor)
        segunda = segunda_franja(valor)
        multip = multiplicador(valor)
        
        opcion1 = get_colores(primera, segunda, multip)
        if valor < 10:
            opcion2 = get_colores(primera, segunda, multip+1)
            opcion3 = get_colores(primera, segunda, multip+2)
            opcion4 = get_colores(primera, segunda, multip+3)
        elif valor < 100:
            opcion2 = get_colores(primera, segunda, multip-1)
            opcion3 = get_colores(primera, segunda, multip+1)
            opcion4 = get_colores(primera, segunda, multip+2)
        elif valor < 1000:
            opcion2 = get_colores(primera, segunda, multip-1)
            opcion3 = get_colores(primera, segunda, multip+2)
            opcion4 = get_colores(primera, segunda, multip+3)
        elif valor < 10000:
            opcion2 = get_colores(primera, segunda, multip-2)
            opcion3 = get_colores(primera, segunda, multip+2)
            opcion4 = get_colores(primera, segunda, multip+3)
        elif valor < 100000:
            opcion2 = get_colores(primera, segunda, multip-3)
            opcion3 = get_colores(primera, segunda, multip+1)
            opcion4 = get_colores(primera, segunda, multip+2)
        else:
            opcion2 = get_colores(primera, segunda, multip-1)
            opcion3 = get_colores(primera, segunda, multip-2)
            opcion4 = get_colores(primera, segunda, multip-3)
        print(text % (valor_tostring(valor), valor_tostring(valor), opcion1, opcion2, opcion3, opcion4))
    print()


main()
