from clasicoaCuantico import *
def main():
    sx = [[ 0, 1 ] ,[ 1, 0 ]]

    sy = [[ 0, -1j] ,[ 1j, 0 ]]

    sz = [[ 1, 0 ] ,[ 0, -1 ]]

    

def mostrarRespuesta4_3_1( observable ):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna los posibles estados que el spin puede transitar despues de ser observado"""

    x,v= Eigen(observable)
    answ = []
    for el in v:
        current = translateEightnVector( el )
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
        eigenValue =  translateValues(x[i])
        eigenVector = translateEightnVector( v[:,i] )
            
        prob =  multiplicarComplejos(eigenValue,[longitud([transicion(eigenVector,shi)])**2,0])
       
        meanValueDistribution = sumarComplejos(meanValueDistribution,prob)
    return meanValueDistribution
      
          

    
main()