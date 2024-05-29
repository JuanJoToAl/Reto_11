# Se declaran e inicializan las listas
matriz_primera : list = []
matriz_segunda : list = []
matriz_final : list = []
multiplicacion_final : list = []
filas : list = []

# Se declaran las variables
num_filas_primera : int
num_columnas_primera : int
num_filas_segunda : int
num_columnas_segunda : int
producto_elemento : float



def llenar_matriz_primera(matriz_primera : list, num_filas_primera : int, 
                          num_columnas_primera : int, filas : list) -> list:

    print(f"La primera matriz se ve de la siguiente forma:")

    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_primera): 

        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas_primera):

        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(
                                    f"Primera matriz: ingrese el número ({i + 1}, {j + 1})"
                                    )))
            
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

    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_segunda): 

        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas_segunda):

        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input((
                                    f"Segunda matriz: ingrese el número ({i + 1}, {j + 1})"
                                    ))))
            
        # Se añade la fila a la matriz
        matriz_segunda.append(filas) 

        # Se imprime la fila para ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_segunda

def multiplicar_matrices(matriz_primera : list, matriz_segunda : list, 
                         multiplicacion_final : list, filas : list) -> list: 
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []

    # Se recorren las filas de la primera matriz
    for i in range(len(matriz_primera)):
        filas = matriz_primera[i]

        # Se recorren las columnas de la segunda matriz
        for j in range(len(matriz_segunda[0])):

            # Se almacenan los elementos de las columnas en la variable 
            columnas = [matriz_segunda[i][j] for i in range(len(matriz_segunda))]

            # Se multiplica una fila por una columna y se suman los resultados 
            producto_elemento = sum(filas[i] * columnas[i] for i in range(len(filas))) 

            # Se almacena el resultado en la lista
            multiplicacion_final.append(producto_elemento)

    print(f"Los elementos de la nueva matriz son: {multiplicacion_final}")
    
    return multiplicacion_final

def llenar_matriz_final(matriz_final : list, num_filas_primera : int, 
                        num_columnas_segunda : int, multiplicacion_final : list, filas: list) -> list:
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []
    print(f"La matriz final se ve de la siguiente forma:")

    # Se recorren las filas de la primera matriz
    for _ in range(num_filas_primera): 

        # Se recorren las columnas de la segunda matriz
        for j in range(num_columnas_segunda):

            # Se ingresan números de la fila a la lista
            filas.append(multiplicacion_final[j])

        # Se eliminan elementos de la fila de la lista
        multiplicacion_final = multiplicacion_final[num_columnas_segunda:]

        # Se añade la fila a la matriz
        matriz_final.append(filas) 

        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_final

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

    # Condicionales para verificar si se pueden multiplicar matrices
    elif num_columnas_primera != num_filas_segunda:
        print("No se pueden multiplicar las matrices porque el número de columnas" 
              " de la primera es diferente al número de filas de la segunda"
              )
        
    else:
        # Llamado de función para llenar la primera matriz
        matriz_primera = llenar_matriz_primera(matriz_primera, num_filas_primera, 
                                               num_columnas_primera, filas)
        
        # Llamado de función para llenar la segunda matriz
        matriz_segunda = llenar_matriz_segunda(matriz_segunda, num_filas_segunda, 
                                               num_columnas_segunda, filas)
        
        # Llamado de función para realizar multiplicaciones
        multiplicacion_final = multiplicar_matrices(matriz_primera, matriz_segunda, 
                                                    multiplicacion_final, filas)
        
        # Llamado de función para llenar matriz final
        matriz_final = llenar_matriz_final(matriz_final, num_filas_primera, 
                                           num_columnas_segunda, multiplicacion_final, 
                                           filas)
        