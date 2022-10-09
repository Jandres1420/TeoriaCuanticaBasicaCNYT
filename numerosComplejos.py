import math
# Para probar las funciones de la segunda entrega usar estas vatiables de listas
# si quiere comprobar su vericidad cambiar los numeros de las listas por los que quieran


def main():
   # sumarComplejos([12, 2], [13, 1])
    #restarComplejos([13, 4], [9, 8])
    #multiplicarComplejos([8, 9], [2, 1])
    #divisionComplejos([8, 9], [2, 1])
    #moduloComplejos([8, -3])
    #cartesianoAPolar([-2, 2])
    #cartesianoAPolar([2, 2])
    #faseComplejos([1, 2])
    ################################################################################################################################################
    ################################################################################################################################################
    # Probando Segunda parte
    # con las nuevas funcione
    # Para probar las funciones de la segunda entrega usar estas vatiables de listas
    # si quiere comprobar su vericidad cambiar los numeros de las listas1 y lista 2 por los numeros que quieran
    # consejo para probar el codigo documentar las funciones que no se estan probando en su momento para no leer todos los metodos en una sola
    # ejecución y confundirse
    lista1 = [1, 3]
    lista2 = [2, 4]
    lista3 = [6, 5]
    sumaDeVectores([lista1, lista2], [lista1, lista2])
    inversoVector([lista2, lista1])
    sumaMatricesComplejas(
        [[lista1, lista1], [lista2, lista2]],
        [[lista2, lista1], [lista1, lista2]])
    inversoMatriz([[lista1], [lista2], [lista3]])
    multiplicarEscalarMatriz(lista3, [[lista1, lista1], [lista2, lista2]])
    transpuestaMatriz([[lista1, lista2, lista3], [lista3, lista2, lista1]])
    conjugadaMatriz([[lista2, lista1, lista3], [lista3, lista2, lista1]])
    adjuntaMatriz([[lista1, lista2, lista3], [lista3, lista2, lista1]])
    multiplicacionDeMarticesIguales(
        [[lista1, lista1], [lista2, lista2]], [[lista2, lista1], [lista1, lista2]])
    accionMatrizVector(
        [[lista1, lista1, lista1], [lista2, lista2, lista2], [lista3, lista3, lista3]], [lista1, lista2, lista3])
    productoInternoVectores([lista1, lista2, lista2], [
                            lista3, lista2, lista3])[0]
    normaVector([[3, 0], [-6, 0], [2, 0]])
    distanciaEntreVectores([lista1, lista2, lista3], [lista3, lista2, lista1])
    matrizHermitaña([[[7, 0], [6, 5]], [[6, -5], [-3, 0]]])


def sumarComplejos(c1, c2):
    suma = [c1[0]+c2[0], c1[1]+c2[1]]
    return suma


def restarComplejos(c1, c2):
    resta = [c1[0]-c2[0], c1[1]-c2[1]]
    return resta


def multiplicarComplejos(c1, c2):
    multiplicacion = [c1[0]*c2[0]-c1[1]*c2[1], c1[1]*c2[0]+c1[0]*c2[1]]
    return multiplicacion


def divisionComplejos(c1, c2):
    dividiendo = c2[0]**2 + c2[1]**2
    division = [(c1[0]*c2[0]+c1[1]*c2[1]) / dividiendo,
                (c2[0]*c1[1]-c1[0]*c2[1]) / dividiendo]


def conjugadoComplejos(c1):
    conjugado = [c1[0], -c1[1]]
    return conjugado


def moduloComplejos(c1):
    modulo = math.sqrt((c1[0])**2 + (c1[1]) ** 2)
    return modulo


def faseComplejos(c1):
    x = c1[0]
    y = c1[1]
    # Encontrando el cuadrante segun los puntos
    if (x < 0 and y < 0) or (x < 0 and y >= 0):
        return math.pi + (math.atan(c1[1] / c1[0]))

    elif x >= 0 and y < 0:
        return 2 * math.pi + (math.atan(c1[1] / c1[0]))

    else:
        return (math.atan(c1[1] / c1[0]))


def cartesianoAPolar(c1):
    angulo = faseComplejos(c1)
    cartesianoAPolar = [moduloComplejos(c1), angulo]
    print(cartesianoAPolar)


def printBonito(respuesta):
    # Se quito el printBonito para mejr
    if (respuesta[1] > 0):
        print(str(respuesta[0]) + " + " + str(respuesta[1]) + "i")
    else:
        print(str(respuesta[0]) + " " + str(respuesta[1]) + "i")
#####################################################################
#####################################################################
#####################################################################
# Empezando segundo laboratorio


def printMatriz(respuesta):
    lista = []


def sumaDeVectores(vect1, vect2):
    if (len(vect1) == len(vect2)):
        for i in range(len(vect1)):
            vect1[i] = sumarComplejos(vect1[i], vect2[i])
        print("Suma de vectores: " + str(vect1))


def inversoVector(vect):
    for x in range(len(vect)):
        actual = vect[x]
        vect[x] = conjugadoComplejos(actual)
        vect[x][0] = - actual[0]
    print("Inverso del vector " + str(vect))
    return vect


def sumaMatricesComplejas(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j] = sumarComplejos(mat1[i][j], mat2[i][j])
    print("suma de matrices complejas : " + str(mat1))
    return mat1


def inversoMatriz(mat):
    for i in range(len(mat)):
        mat[i] = inversoVector(mat[i])
    print("inverso de Matriz " + str(mat))
    return mat


def multiplicarEscalarMatriz(c1, mat):
    lista = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):

            lista.append(multiplicarComplejos(c1, mat[i][j]))
    print("multiplicacion Escalar por matriz " + str(lista))
    return lista


def accionMatrizVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [[0, 0] for x in range(row)]

        for i in range(row):
            for j in range(col):

                mult = multiplicarComplejos(matrix[i][j], vector[j])
                answ[i] = sumarComplejos(answ[i], mult)
        print("Accion entre matriz vector " + str(answ))
        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


def transpuestaMatriz(matrix):
    answ = [[0 for x in range(len(matrix))] for t in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            answ[i][j] = matrix[j][i]
    print("Transpuesta de la matriz " + str(answ))
    return answ


def conjugadaMatriz(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = conjugadoComplejos(matrix[i][j])
    print("La matriz conjugada es " + str(matrix))
    return matrix


def adjuntaMatriz(matrix):
    print("La adjunta de la matriz es " +
          str(conjugadaMatriz(transpuestaMatriz(matrix))))
    return conjugadaMatriz(transpuestaMatriz(matrix))


def multiplicacionDeMarticesIguales(mat1, mat2):

    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])
    if (col1 == row2):
        answ = [[(0, 0) for t in range(col2)] for x in range(row1)]
        for i in range(row1):
            for j in range(col2):

                current = (0, 0)

                for k in range(row2):

                    mult = multiplicarComplejos(mat1[i][k], mat2[k][j])

                    current = sumarComplejos(current, mult)

                answ[i][j] = current
        print("El producto de dos matrices es " + str(answ))
        return answ


def productoInternoVectores(vector1, vector2):
    answ = [0, 0]
    for x in range(len(vector1)):
        answ = sumarComplejos(
            answ, multiplicarComplejos(vector1[x], vector2[x]))
    print("Producto interno es " + str(answ))
    return answ


def normaVector(vector):
    print("La norma del vector es: " +
          str(math.sqrt(abs(productoInternoVectores(vector, vector)[0]))))
    return math.sqrt(abs(productoInternoVectores(vector, vector)[0]))


def restaDeVectores(vect1, vect2):
    if (len(vect1) == len(vect2)):
        lista = []
        for i in range(len(vect1)):
            vect1[i] = restarComplejos(vect1[i], vect2[i])
        print("Resta de vectores " + str(vect1))
        return (vect1)


def distanciaEntreVectores(vector1, vector2):
    print("Distancia entre vectores " +
          str(normaVector(restaDeVectores(vector1, vector2))))
    return normaVector(restaDeVectores(vector1, vector2))


def matrizHermitaña(matrix):
    flag = False
    adjunta = adjuntaMatriz(matrix)
    if (adjunta == matrix):
        flag = True
    print("La matriz es hermitaña " + str(flag))
    return flag

def vectorAdjunta( vector ):
    for x in range( len( vector )):
        vector[x] = conjugadoComplejos( vector[x])
    return vector


def multVector(vect1, vect2):
    acu = [0, 0]
    for c in range(len(vect1)):
        acu = sumaDeVectores(acu, multiplicarComplejos(vect1[c], vect2[c]))
    return acu

def internalProduct( vector1 , vector2 ):
    return multVector( vectorAdjunta( vector1),  vector2 )


def restaMatrices(mat1, mat2):
    row, colum = len(mat1), len(mat1[0])

    for i in range(row):
        mat1[i] = restaDeVectores(mat1[i], mat2[i])
    return mat1

def matrizIdentidad( matrix ):
    row,  column  = len( matrix ) , len( matrix[ 0 ] )
    
    matrix=[[[] for i in range( column )] for j in range( row )]
    
    for i in range( row ):
        for j in range(  column ):
            if i==j:
                matrix[ i ][ j ] =  [ 1,0]
            else:
                matrix[ i ][ j ] =  [ 0,0 ]
    return matrix

def multiplicaMatriz( mat1, mat2 ):

    row1, col1 = len( mat1 ),len( mat1[ 0 ] )
    row2, col2 =  len( mat2 ), len( mat2[ 0 ] )
     
    if ( col1 == row2 ):
        
        answ = [ [  ( 0,0 )  for t in range( col2 ) ] for x in range( row1 ) ]
        
        for i in range( row1 ):
            for j in range( col2 ):
                
                current = ( 0, 0 ) 
                
                for k in range( row2 ):

                    mult =  multiplicarComplejos( mat1[ i ][ k ], mat2[ k ][ j ]  ) 
                    
                    current =  sumarComplejos( current , mult ) 
                    
                answ[ i ][ j ]  = current

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def esUnitaria( matrix ):
    row, col = len( matrix ), len( matrix[ 0 ] )
    
    if row == col :
        adjoint = adjuntaMatriz( matrix )
        
        return ( multiplicaMatriz( matrix , adjoint) == matrizIdentidad( matrix ) )or ( multiplicaMatriz( matrix , adjoint)  == multiplicaMatriz( adjoint , matrix) )
        
main()
