from clasicoaCuantico import *
def main():
    sx = [[ 0, 1 ] ,[ 1, 0 ]]

    sy = [[ 0, -1j] ,[ 1j, 0 ]]

    sz = [[ 1, 0 ] ,[ 0, -1 ]]

    print("Mostrar respuesta 4_3_1 sx " + str(mostrarRespuesta4_3_1(sx)))
    print("Mostrar respuesta 4_3_1 sy " + str(mostrarRespuesta4_3_1(sy)))
    print("Mostrar respuesta 4_3_1 sz " + str(mostrarRespuesta4_3_1(sz)))
    
    print("Mostrar respuesta 4.3.2 sx " + str(mostrarRespuesta4_3_2(sx)))
    print("Mostrar respuesta 4.3.2 sy " + str(mostrarRespuesta4_3_2(sy)))
    print("Mostrar respuesta 4.3.2 sz " + str(mostrarRespuesta4_3_2(sz)))
    
    raiz = math.sqrt(2)/2
    u1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    u2 = [[[raiz, 0], [raiz, 0]], [[raiz, 0], [-raiz, 0]]]
    print("Mostrar respuesta 4.4.1 u1" + str(esUnitaria(u1)))
    print("Mostrar respuesta 4.4.1 u2" + str(esUnitaria(u2)))
    
    print("Mostrar respuesta 4.4.1 u1" + str(multiplicaMatriz(u1,u2)))
    print("Mostrar respuesta 4.4.1 u2" + str(multiplicaMatriz(u1, u2)))
    
    raiz = 1/math.sqrt(2)
    vectIni = [[1, 0], [0, 0], [0, 0], [0, 0]]
    matrix = [[[0, 0], [raiz, 0], [raiz, 0], [0, 0]],
              [[0, raiz], [0, 0], [0, 0], [raiz, 0]],
              [[raiz, 0], [0, 0], [0, 0], [0, raiz]],
              [[0, 0], [raiz, 0], [-raiz, 0], [0, 0]]]
    
    print("Mostrar respuesta 4.4.2 " +
          str(multipleRendijaCuantico(matrix, vectIni, 3)))


def mostrarRespuesta4_3_1( observable ):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna los posibles estados que el spin puede transitar despues de ser observado"""

    x,v= Eigen(observable)
    answ = []
    for el in v:
        current = traducirEigen(el)
        answ.append(current)
    print(answ)
    return answ

def mostrarRespuesta4_3_2( observable ):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna la media de la distribucion del spin ingresado"""

    shi = [ [1,0],[0,0] ]
    x,v= Eigen( observable  )

    meanValueDistribution = [0,0]
    for i in range( len(x) ):
        eigenValue = traducirValores(x[i])
        eigenVector = traducirEigen(v[:, i])
            
        prob =  multiplicarComplejos(eigenValue,[longitud([transicion(eigenVector,shi)])**2,0])
       
        meanValueDistribution = sumarComplejos(meanValueDistribution,prob)
    return meanValueDistribution
      
          

    
main()