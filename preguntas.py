"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
file1 = open("data.csv", 'r')
lines = file1.readlines()

lista=[]
for line in lines:
    lista=lista+[line.replace("\n","").split("\t")]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    for element in lista:
        suma=suma+int(element[1])
    
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras=list(set([z[0] for z in lista]))
    letras.sort()
    cuenta=[]

    for letra in letras:
        cant=0
        for element in lista:
            if element[0]==letra:
                cant=cant+1
        tupla=(letra,cant)        
        cuenta=cuenta+[tupla]    
    return cuenta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras=list(set([z[0] for z in lista]))
    letras.sort()
    suma2=[]

    for letra in letras:
        sum2=0
        for element in lista:
            if element[0]==letra:
                sum2=sum2+int(element[1])
        tupla=(letra,sum2)        
        suma2=suma2+[tupla]
    return suma2


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses=[z[2].split('-')[1] for z in lista]
    cuentameses=[]
    for mes in list(set(meses)):
        cuenta=meses.count(mes)
        tupla=(mes,cuenta)
        cuentameses=cuentameses+[tupla]
    cuentameses.sort()
    
    return cuentameses


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    numeros=[z[1] for z in lista]
    letras=list(set([z[0] for z in lista]))
    letras.sort()
    maximin=[]
    for letra in letras:
        mini=max(numeros)
        maxi=min(numeros)
        for element in lista:
            if element[1] < mini and element[0] == letra:
                mini=element[1]
            if element[1] > maxi and element[0] == letra:
                maxi=element[1]
        tupla=(letra,int(maxi),int(mini))
        maximin=maximin+[tupla]
    return maximin


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    columna=[(z[4].split(',')) for z in lista]
    pares=[]
    for clave in range(0, len(columna)):
        for element in range(0, len(columna[clave])):
            pares.append([(columna[clave][element][:3]),int(columna[clave][element][4:])])
    claves=list(set([z[0] for z in pares]))
    numeros=[z[1] for z in pares]
    claves.sort()
    maximin=[]
    for clave2 in claves:
        mini=max(numeros)
        maxi=min(numeros)
        for par in pares:
            if par[1] < mini and par[0] == clave2:
                mini=par[1]
            if par[1] > maxi and par[0] == clave2:
                maxi=par[1]
        tupla=(clave2,int(mini),int(maxi))
        maximin=maximin+[tupla]
    return maximin


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letras=([z[0] for z in lista])
    numeros=list(set([z[1] for z in lista]))
    numeros.sort()
    numletra=[]
    for numero in numeros:
        listado=[]
        for element in lista:
            if element[1] == numero:
                listado.append(element[0])
        tupla=(int(numero),(listado))
        numletra=numletra+[tupla]
    return numletra



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letras=([z[0] for z in lista])
    numeros=list(set([z[1] for z in lista]))
    numeros.sort()
    numletra=[]
    for numero in numeros:
        listado=[]
        for element in lista:
            if element[1] == numero:
                listado.append(element[0])
        tupla=(int(numero),sorted(list(set(listado))))
        numletra=numletra+[tupla]
    return numletra


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    columna=[(z[4].split(',')) for z in lista]
    pares=[]
    for clave in range(0, len(columna)):
        for element in range(0, len(columna[clave])):
            pares.append([(columna[clave][element][:3])])
    claves=list(set([z[0] for z in pares]))
    claves.sort()
    cuentaclave={}
    for clave2 in claves:
        contador=0
        for par in pares:
            if par[0] == clave2:
                contador=contador+1
        diccionario={clave2:contador}
        cuentaclave.update(diccionario)
    return cuentaclave


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    
    resultado=[]
    for element in lista:
        resultado.append((element[0],len(element[3].split(',')),len(element[4].split(','))))
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    columna2=[z[3].split(',') for z in lista]
    pares=[]
    for clave in columna2:
        pares=pares+clave
    claves=list(set(pares))
    claves.sort()
    columna=[(z[3].split(','),z[1]) for z in lista]
    diccionario={}
    for clave in claves:
        suma=0
        for element in columna:
            for letra in element[0]:
                if letra == clave:
                    suma=suma+int(element[1])
        dic={clave:suma}
        diccionario.update(dic)
    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras=list(set([z[0] for z in lista]))
    letras.sort()
    columna=[(z[0],sum([int(x[4:]) for x in z[4].split(',')])) for z in lista]
    diccionario={}
    for letra in letras:
        suma=0
        for element in columna:
            if element[0] == letra:
                suma=suma+element[1]
        dic={letra:suma}
        diccionario.update(dic)
    return diccionario
