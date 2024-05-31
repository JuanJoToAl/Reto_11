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
    """
    Esta función llena una matriz con valores ingresados por el 
    usuario fila por fila y muestra la matriz a medida que se construye.
    
    Args:
        matriz_primera (list): Es una lista que almacenará los valores de la
        primera matriz que el usuario ingresará.

        num_filas_primera (int): Representa el número de filas de la matriz.
        Este valor se utiliza para determinar cuántas veces se repetirá el
        bucle para completar los valores de cada fila de la matriz.
        
        num_columnas_primera (int): El parámetro `num_columnas_primera` 
        representa el número de columnas de la matriz. 
        
        filas (list): Es una lista que se utiliza para almacenar los elementos 
        de cada fila de la matriz que está llenando el usuario.
    
    Returns:
        Se devuelve la primera matriz llena como una lista de listas.
    """

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
    """
    La función toma la entrada del usuario para llenar una segunda matriz 
    con un número específico de filas y columnas.
    
    Args:
        matriz_segunda (list): Es una lista que almacena los valores de la 
        segunda matriz. 
        
        num_filas_segunda (int): Representa el número de filas en la
        segunda matriz. 

        num_columnas_segunda (int): Representa el número de columnas
        en la segunda matriz. 
        
        filas (list): Es una lista que se utiliza para almacenar los 
        números que irán en cada fila de la segunda matriz. 

    Returns:
        Devuelve la `matriz_segunda` actualizada después de llenarla
        con los valores ingresados por el usuario.
    """
    
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
    """
    La función `multiplicar_matrices` toma dos matrices como entrada, 
    las multiplica y devuelve la matriz resultante.
    
    Args:
        matriz_primera (list): Representa la primera matriz que se desea
        multiplicar con la segunda matriz (`matriz_segunda`).
        
        matriz_segunda (list): Representa la segunda matriz que se desea
        multiplicar con la primera matriz (`matriz_primera`).
        
        multiplicacion_final (list): Es una lista que se utiliza para
        almacenar los resultados de multiplicar las dos matrices 
        `matriz_primera` y `matriz_segunda`.
        
        filas (list): Almacena las filas de la primera matriz durante el 
        proceso de multiplicación de matrices.

    
    Returns:
        Devuelve la lista `multiplicacion_final` que contiene
        los elementos de la multiplicación de las dos matrices de entrada
        `matriz_primera` y `matriz_segunda`.
    """
    
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
                        num_columnas_segunda : int, multiplicacion_final : list, 
                        filas: list) -> list:
    """
    Esta función llena una matriz final multiplicando dos matrices.
    
    Args:
        matriz_final (list): Matriz donde se almacenanlos resultados 
        finales de las multipliciones entre matrices
        
        num_filas_primera (int): Representa el número de filas de la
        primera matriz. Este valor se utiliza para determinar el número 
        de iteraciones al llenar la matriz final.

        num_columnas_segunda (int): Representa el número de columnas
        en la segunda matriz. Este valor se utiliza para determinar el 
        número de columnas a iterar al llenar la matriz final.

        multiplicacion_final (list): Representa una lista de listas con los
        números que son el resultado de multiplicar elementos de la primera 
        y segunda matriz. 

        filas (list): Es una lista que se utiliza para almacenar los elementos 
        de cada fila de la matriz final que se construye.

    Returns:
        La función devuelve la matriz final después de llenarla con los valores
        de la multiplicación de la primera y segunda matriz.
    """
    
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
        