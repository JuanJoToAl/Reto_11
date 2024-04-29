# Se declaran e inicializan las listas
matriz_primera : list = []
matriz_segunda : list = []
matriz_suma : list = []
matriz_resta : list = []
filas : list = []
# Se declaran las variables
num_filas_primera : int
num_columnas_primera : int
num_filas_segunda : int
num_columnas_segunda : int
suma_filas : list
resta_filas : list



def llenar_matriz_primera(matriz_primera : list, num_filas_primera : int, 
                          num_columnas_primera : int, filas : list) -> list:

    print(f"La primera matriz se ve de la siguiente forma:")
    # Se recorren la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_primera): 
        # Se recorren la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas_primera):
        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(f"Ingrese un número ({i + 1}, {j + 1})")))
        # Se añade la fila a la matriz
        matriz_primera.append(filas) 
        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")
        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_primera

def llenar_matriz_segunda(matriz_segunda : list, num_filas_segunda : int, 
                          num_columnas_segunda : int, filas : list) -> list:
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []
    print(f"La segunda matriz se ve de la siguiente forma:")
    # Se recorren la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_segunda): 
        # Se recorren la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas_segunda):
        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input((f"Ingrese un número ({i + 1}, {j + 1})"))))
        # Se añade la fila a la matriz
        matriz_segunda.append(filas) 
        # Se imprime la fila para ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")
        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_segunda

def sumar_matrices(matriz_primera, matriz_segunda, 
                   matriz_suma : list) -> list:
    print("La suma de las matrices se ve de la siguiente forma:")
    # Se recorren las filas de las matrices
    for i in range(len(matriz_primera)):
        # Se vacía la lista "suma_filas" para no interferir en la suma
        suma_filas = [] 
        # Se recorren las las columnas de las matrices
        for j in range(len(matriz_primera)):
            # Se suman los valores según su fila y columna
            suma_filas.append(matriz_primera[i][j] + matriz_segunda[i][j]) 
        # Se imprime la fila para ver cómo se contruye la matriz
        print(suma_filas)
        # Se agrega la fila a la matriz final
        matriz_suma.append(suma_filas)
        
        
    return matriz_suma

def restar_matrices(matriz_primera, matriz_segunda, 
                   matriz_resta : list) -> list:
    print("La resta de las matrices se ve de la siguiente forma:")
    # Se recorren las filas de las matrices
    for i in range(len(matriz_primera)):
        # Se vacía la lista "resta_filas" para no interferir en la suma
        resta_filas = []
        # Se recorren las las columnas de las matrices
        for j in range(len(matriz_primera)):
            # Se restan los valores según su fila y columna
            resta_filas.append(matriz_primera[i][j] - matriz_segunda[i][j]) 
        # Se imprime la fila para ver cómo se contruye la matriz
        print(resta_filas)
        # Se agrega la fila a la matriz final
        matriz_resta.append(resta_filas)
        
        
    return matriz_resta

if __name__ == "__main__":
    # Solicitud: número de filas y columnas de la primera matriz
    num_filas_primera = int(input("Primera matriz: ingrese número de filas"))
    num_columnas_primera = int(input("Primera matriz: ingrese número de columnas"))
    # Solicitud: número de filas y columnas de la segunda matriz
    num_filas_segunda = int(input("Segunda matriz: ingrese número de filas"))
    num_columnas_segunda = int(input("Segunda matriz: ingrese número de columnas"))
    # Primera matriz: condicional para input de matrices con orden cero
    if num_filas_primera == 0 and num_columnas_primera == 0:
        print("La primera matriz no tiene filas ni columnas :(")
    # Primera matriz: condicional para input de matrices con orden negativo
    elif num_filas_primera < 0 or num_columnas_primera < 0:
        print("Primera matriz: cantidad negativa de columnas/filas no es permitida")
    # Segunda matriz: condicional para input de matrices con orden cero
    elif num_filas_segunda == 0 and num_columnas_segunda == 0:
        print("La segunda matriz no tiene filas ni columnas :(")
    # Segunda matriz: condicional para input de matrices con orden negativo
    elif num_filas_segunda < 0 or num_columnas_segunda < 0:
        print("Segunda matriz: cantidad negativa de columnas/filas no es permitida")
    # Condicionales para verificar si se pueden sumar matrices
    elif num_filas_primera != num_filas_segunda :
        if num_columnas_primera != num_columnas_segunda:
            print("No se pueden sumar las matrices porque no son del mismo orden")

    elif num_columnas_primera != num_columnas_segunda:
        print("No se puede sumar las matrices porque no son del mismo orden")
        
    else:
        # Llamado de función para llenar la primera matriz
        matriz_primera = llenar_matriz_primera(matriz_primera, num_filas_primera, 
                                               num_columnas_primera, filas)
        # Llamado de función para llenar la segunda matriz
        matriz_segunda = llenar_matriz_segunda(matriz_segunda, num_filas_segunda, 
                                               num_columnas_segunda, filas)
        # Llamado de función para sumar matrices
        matriz_suma = sumar_matrices(matriz_primera, matriz_segunda, matriz_suma)
        # Llamado de función para restar matrices
        matriz_resta = restar_matrices(matriz_primera, matriz_segunda, matriz_resta)
        