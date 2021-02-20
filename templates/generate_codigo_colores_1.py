import re

def filename(valor):
    basename = 'electric-resistencia-'
    if valor < 10:
        return basename + re.sub('\.', '_', str(valor)) + '.png'
    return basename + str(valor) + '.png'


def primera_franja(valor):
    return int(str(valor)[0])

def segunda_franja(valor):
    return int(str(valor*1000)[1])

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


def valor_tostring(a, b, m):
    valor = (a * 10.0 + b)*pow(10.0, m)
    if valor<10:
        return str(round(valor, 1)) 
    if valor<100:
        return str(int(round(valor, 0)))
    if valor<1000:
        return str(int(round(valor, 0)))
    if valor<10000:
        return str(round(valor/1000.0, 1)) + 'k'
    if valor<100000:
        return str(int(round(valor/1000.0, 0))) + 'k'
    if valor<1000000:
        return str(int(round(valor/1000.0, 0))) + 'k'
    if valor<10000000:
        return str(round(valor/1000000.0, 1)) + 'M'
    return str(int(round(valor/1000000.0, 0))) + 'M'


def valor_tostring3(a, b, c):
    valor = a*100.0 + b*10.0 + c
    return str(int(round(valor, 0)))

def next(valor):
    if valor >= 9:
        return 0
    return valor + 1

def prev(valor):
    if valor <= 1:
        return 9
    return valor -1
    
text = """
- Title: Código de colores %s Ohmios
  Question: ¿Qué valor tiene esta resistencia?
  Image: images/%s
  Image_width: 320
  Choices:
    - %s
    - %s
    - %s
    - %s
"""


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
        
        imagen = filename(valor)
        opcion1 = '%sΩ' % (valor_tostring(primera, segunda, multip))
        if valor < 10:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip+1))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip+3))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip+2))
        elif valor < 100:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip-1))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip+3))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip))
        elif valor < 1000:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip-1))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip+2))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip))
        elif valor < 10000:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip-2))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip+1))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip))
        elif valor < 100000:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip-3))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip+2))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip))
        else:
            opcion2 = '%sΩ' % (valor_tostring(primera, segunda, multip-1))
            opcion3 = '%sΩ' % (valor_tostring(primera, segunda, multip-3))
            opcion4 = '%sΩ' % (valor_tostring3(primera, segunda, multip))
        print(text % (valor, imagen, opcion1, opcion2, opcion3, opcion4))
    print()


main()
