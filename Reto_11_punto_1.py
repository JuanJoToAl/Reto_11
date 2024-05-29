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




def llenar_matriz_primera(matriz_primera : list, num_filas_primera : int, 
                          num_columnas_primera : int, filas : list) -> list:
    """
    La función `llenar_matriz_primera` toma la entrada del usuario para llenar una matriz con
    dimensiones específicas y devuelve la matriz llena.
    
    Args:
      matriz_primera (list): El parámetro `matriz_primera` es una lista que almacenará los elementos de
      la primera matriz que está llenando el usuario.

      num_filas_primera (int): El parámetro `num_filas_primera` representa el número de filas de la
      matriz. 

      num_columnas_primera (int): `num_columnas_primera` es el número de columnas en la primera matriz
      que el usuario necesita ingresar. 

      filas (list): El parámetro `filas` en la función `llenar_matriz_primera` es una lista que se
      utiliza para almacenar los elementos de cada fila de la matriz. 
    
    Returns:
      La función `llenar_matriz_primera` devuelve la matriz llena `matriz_primera` después de que el
      usuario haya ingresado los números para cada celda de la matriz.
    """

  
    print(f"La primera matriz se ve de la siguiente forma:")

    # Se recorren la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_primera): 

        # Se recorren la cantidad de columnas ingresadas por el usuario
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
    """
    Esta función de Python llena una segunda matriz con valores ingresados 
    por el usuario según el número especificado de filas y columnas.
    
    Args:
        matriz_segunda (list): El parámetro `matriz_segunda` es una lista 
        que almacenará los elementos de la primera matriz que está llenando 
        el usuario.
        
        num_filas_segunda (int): El parámetro `num_filas_segunda` representa 
        el número de filas en la segunda matriz. 

        num_columnas_segunda (int): El parámetro `num_columnas_segunda` 
        representa el número de columnas en la segunda matriz. 

        filas (list): El parámetro `filas` es una lista que se utiliza para 
        almacenar los números que irán en cada fila de la segunda matriz. 
        
    Returns:
        La función `llenar_matriz_segunda` devuelve la `matriz_segunda` 
        actualizada después de llenarla con los valores ingresados por 
        el usuario.
    """
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []
    print(f"La segunda matriz se ve de la siguiente forma:")

    # Se recorren la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_segunda): 

        # Se recorren la cantidad de columnas ingresadas por el usuario
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

def sumar_matrices(matriz_primera : list, matriz_segunda : list, 
                   matriz_suma : list, filas : list) -> list: 
    """
    Esta función toma dos matrices como entrada, suma sus elementos 
    correspondientes y devuelve la matriz resultante.
    
    Args:
        matriz_primera (list): Representa la primera matriz que se agregará.
        
        matriz_segunda (list): Representa la segunda matriz que desea agregar a
        la primera matriz (`matriz_primera`).
        
        matriz_suma (list): Es una lista que almacenará el resultado de sumar
        las matrices `matriz_primera` y `matriz_segunda`.
        
        filas (list): Almacena la suma de elementos de las posiciones
        correspondientes en las dos matrices de entrada `matriz_primera` y
        `matriz_segunda`.
    
    Returns:
        Se retorna la matriz final `matriz_suma`, resultado de sumar
        las dos matrices de entrada `matriz_primera` y `matriz_segunda`.
    """
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []
    print("La suma de las matrices se ve de la siguiente forma:")

    # Se recorren las filas de las matrices
    for i in range(len(matriz_primera)):

        # Se recorren las las columnas de las matrices
        for j in range(len(matriz_primera)):

            # Se suman los valores según su fila y columna
            filas.append(matriz_primera[i][j] + matriz_segunda[i][j]) 

        # Se imprime la fila para ver cómo se contruye la matriz
        print(filas)

        # Se agrega la fila a la matriz final
        matriz_suma.append(filas)

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []
        
        
    return matriz_suma

def restar_matrices(matriz_primera : list, matriz_segunda : list, 
                    matriz_resta : list, filas : list) -> list:
    """
    Esta función resta dos matrices por elementos y 
    devuelve la matriz resultante.
    
    Args:
        matriz_primera (list): Representa la primera matriz que se agregará.
        
        matriz_segunda (list): Representa la segunda matriz que desea restar a
        la primera matriz (`matriz_primera`).
        
        matriz_resta (list): Es una lista que almacenará el resultado de restar
        las matrices `matriz_primera` y `matriz_segunda`.
        
        filas (list): Almacena la resta de elementos de las posiciones
        correspondientes en las dos matrices de entrada `matriz_primera` y
        `matriz_segunda`.
    
    Returns:
        Se retorna la matriz final `matriz_resta`, resultado de restar
        las dos matrices de entrada `matriz_primera` y `matriz_segunda`.
    """
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = []
    print("La resta de las matrices se ve de la siguiente forma:")

    # Se recorren las filas de las matrices
    for i in range(len(matriz_primera)):

        # Se recorren las las columnas de las matrices
        for j in range(len(matriz_primera)):

            # Se restan los valores según su fila y columna
            filas.append(matriz_primera[i][j] - matriz_segunda[i][j]) 

        # Se imprime la fila para ver cómo se contruye la matriz
        print(filas)

        # Se agrega la fila a la matriz final
        matriz_resta.append(filas)

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []
        
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
        matriz_suma = sumar_matrices(matriz_primera, matriz_segunda, 
                                     matriz_suma, filas) 
        
        # Llamado de función para restar matrices
        matriz_resta = restar_matrices(matriz_primera, matriz_segunda, 
                                       matriz_resta, filas) 
        