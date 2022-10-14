from numerosComplejos import *
import matplotlib.pyplot as plot
import numpy as np
def main():
    
    booleanMatrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                     [True, False, False, False, False, False], [
        False, False, True, False, False, False],
        [False, False, False, True, False, False], [False, False, False, False, True, False]]

    vectIni = [True, False, False, False, False, False]
    print("Experimento canicas " + str(experimentoCanicas(1, booleanMatrix[:], vectIni[:])))
    
    matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.5, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.5, 0], [0.5, 0], [0, 0],
               [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [0.5, 0], [0.5, 0],
               [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [0, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

    vectIni = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    
    print("Multiple rendija clasico  " +
          str(multipleRendijaClasico(matrix[:], vectIni[:], 1)))
    
    matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.7071067811865475, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.7071067811865475, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [-0.4082482904638631, 0.4082482904638631],
               [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [-0.4082482904638631, -0.4082482904638631],
               [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.4082482904638631, -0.4082482904638631], [-0.4082482904638631,
                                                                   0.4082482904638631], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [-0.4082482904638631, -0.4082482904638631],
               [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
              [[0, 0], [0, 0], [0.4082482904638631, -0.4082482904638631], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

    vectIni = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    
    print("Multiple rendija cuantico  " + str(multipleRendijaCuantico(matrix[:], vectIni[:], 1)))
    
    Matriz_Doble_Rendija = [
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0], [0, 0], [0, 0]],
        [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)],
            [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)],
            [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6),
                                                         1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)],
            [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

    Estado_Inicial = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    answ = accionMatrizVector(multipleRendijaCuantico(Matriz_Doble_Rendija[:],
                                                              Estado_Inicial[:], 2),  Estado_Inicial)
    graphProbabilitiesVector(answ)
    

def accionBooleanentreMatrizVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [False for c in range(row)]

        for i in range(row):
            And = True

            for j in range(col):
                And = matrix[i][j] and vector[j]
                answ[i] = answ[i] or And

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def experimentoCanicas( clicks ,booleanMatrix, vectIni  ):
    if ( clicks >= 0 and type( clicks ) is int ):
        for c in range( clicks ):
            vectIni = accionBooleanentreMatrizVector(booleanMatrix, vectIni)
        return vectIni


def multipleRendijaClasico(matrix, vectIni, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        for x in range(clicks):
            vectIni = accionMatrizVector(matrix, vectIni)
        return vectIni
    return -1


def multipleRendijaCuantico(matrix, vectIni, clicks):
    if ( clicks  >= 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        copyMatrix = matrix[:]
        
        for x in range(clicks  ):
            matrix = multiplicacionDeMarticesIguales( matrix, copyMatrix)

        return matrizFinal(matrix)
    return -1


def graphProbabilitiesVector( vector  ):
    x = np.array([x for x in range(len(vector))])
    y = np.array([round(vector[x][0]*100, 2) for x in range(len(vector))])

    plot.bar( x,y , color ='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()
  
  

def matrizFinal(matrix):
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(moduloComplejos(matrix[i][j])**2), 0])

        matrix[i] = nRow
    return matrix

###### Observablees 
###### Observablees 
###### Observablees 
###### Observablees

def dosDecimales(num, oneDecimal):
    num = "{:.2f}".format(num)
    num = (num[:-1] if oneDecimal else num)
    return float(num)


def longitud(vect):
    """Calcula la longitud de un vector dado"""
    acu = 0
    for x in range(len(vect)):
        acu += (moduloComplejos(vect[x]))**2
    return math.sqrt(acu)


def normaliza(vect):
    """normaliza un vector dado """
    length = longitud(vect)
    for x in range(len(vect)):
        vect[x] = [vect[x][0]/length, vect[x][1]/length]
    return vect


def bra(vect):
    """Devuelve el bra de un vector dado"""
    return vectorAdjunta(vect)


def transicion(vect1, vect2):
    """Nos dice cuanto es la transicion de un vector a otro"""
    ##(rvs hc)  el bra a vect1
    return internalProduct(vect1, vect2)


def probabilidad(vector, position):
    """Calcula la probabilidad de que un vector este en el estado dado( posicion )"""
    length = longitud(vector)
    if (0 <= position < len(vector)):
        return dosDecimales(moduloComplejos(vector[position])**2 / length**2, False)


def OmegaPsi(psi, omega):
    return internalProduct(accionMatrizVector(omega, psi), psi)[0]


def DeltaPsi(omega, expectedValue):

    return restaMatrices(omega, multiplicarEscalarMatriz(expectedValue, matrizIdentidad(omega)))


def matrixPsi(matrix, psi):
    ## rvs pq al llmse 2 veces cmba
    accionMatrizVector(matrix, vectorAdjunta(psi))
    vect = accionMatrizVector(matrix, adjuntaMatriz(psi))

    ##n dbra ser    (psi) adjoint sino psi.

    return dosDecimales(multVector(vect, vectorAdjunta(psi))[0], False)


def variance(psi, omega):
    expectedValue = dosDecimales(OmegaPsi(psi, omega), True)
    deltaPsi = DeltaPsi(omega, [expectedValue, 0.0])
    matrixOfVariance = multiplicaMatriz(deltaPsi, deltaPsi)
    return matrixPsi(matrixOfVariance, psi)


def describeAnObservable(psi, matrix):
    if (matrizHermitaña(matrix)):
        mean = dosDecimales(OmegaPsi(psi, matrix), True)

        return [variance(psi, matrix), mean]
    return None


def traducirEigen(vector):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    answ = []
    for el in vector:
        answ.append([el.real, el.imag])
    return answ


def traducirValores(val):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    return [val.real, val.imag]


def Eigen(omega):
    # x Eigenvalor, v Eigenvector = Alg.eig(matrix), donde Alg es la libreria linalg
    observable = np.array(omega)
    x, v = np.linalg.eig(observable)

    return x, v

    
main()