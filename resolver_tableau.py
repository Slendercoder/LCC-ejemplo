#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print "Importando tableaux"
import Tableaux as T

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

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

conjunciones = '8-6-Y1>' + conjunciones + 'Y'
conjunciones = '9-7-Y2>' + conjunciones + 'Y'
conjunciones = '8-4-Y3>' + conjunciones + 'Y'
conjunciones = '9-3-Y4>' + conjunciones + 'Y'
conjunciones = '7-1-Y6>' + conjunciones + 'Y'
conjunciones = '6-2-Y7>' + conjunciones + 'Y'
conjunciones = '3-1-Y8>' + conjunciones + 'Y'
conjunciones = '4-2-Y9>' + conjunciones + 'Y'

# Creo la formula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
# print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, interpretaciones = T.Tableaux(lista_hojas, letrasProposicionales)

if OK == 'Satisfacible':
    if len(interpretaciones) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        import visualizacion as V
        contador = 1
        for i in interpretaciones:
            V.dibujar_tablero(i,contador)

print "Proceso terminado!"
