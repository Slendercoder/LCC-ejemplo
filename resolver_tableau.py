#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print "Importando paquetes..."
from timeit import default_timer as timer
import os
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres caballos
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    # print "aux1: ", aux1
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        # print "aux2", aux2
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x != r]
            for k in aux3:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

        # print "Conjunciones: ", conjunciones

# Regla 2: Ningun caballo debe poder atacar a otro

# conjunciones = '8-6-Y1>' + conjunciones + 'Y'
# conjunciones = '9-7-Y2>' + conjunciones + 'Y'
# conjunciones = '8-4-Y3>' + conjunciones + 'Y'
# conjunciones = '9-3-Y4>' + conjunciones + 'Y'
# conjunciones = '7-1-Y6>' + conjunciones + 'Y'
# conjunciones = '6-2-Y7>' + conjunciones + 'Y'
# conjunciones = '3-1-Y8>' + conjunciones + 'Y'
# conjunciones = '4-2-Y9>' + conjunciones + 'Y'

# Creo la formula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        # Eliminamos repeticiones dentro de cada interpretacion
        INTS = [list(set(i)) for i in INTS]
        # Eliminamos interpretaciones repetidas
        INTS_set = set(tuple(x) for x in INTS)
        INTS = [list(x) for x in INTS_set]
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion as V
        contador = 1
        for i in interpretaciones:
            V.dibujar_tablero(i,contador)

print "FIN"
