# Se declaran e inicializan las listas
matriz : list = []
matriz_traspuesta : list = []
filas : list = []

# Se declaran las variables
num_filas : int
num_columnas : int

def llenar_matriz(matriz : list, num_filas : int, num_columnas : int, filas : list) -> list:
    """
    La función `llenar_matriz` toma una lista que representa una matriz y 
    la llena con los parámetros ingresados por el usuario y devuelve la 
    matriz completa.
    
    Args:
        matriz (list): Es una lista que almacenará los elementos de la 
        matriz que se va a llenar.

        num_filas (int): Representa el número de filas en la matriz que el
        usuario desea crear.

        num_columnas (int): Representa el número de columnas en la matriz que
        el usuario desea crear.

        filas (list): Es una lista que se usa para almacenar los números que 
        el usuario ingresa para cada fila de la matriz. 
    
    Returns:
        Se devuelve la matriz llena como una lista de listas después de que 
        el usuario haya ingresado los números para cada celda de la matriz.
    """

    print(f"La matriz se ve de la siguiente forma:")

    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas): 

        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas):

        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(f"Ingrese el número ({i + 1}, {j + 1})")))

        # Se añade la fila a la matriz
        matriz.append(filas) 

        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz

def trasponer_matriz(num_filas : int, num_columnas : int, 
                     filas : list, matriz : list) -> list:
    """
    Esta función de Python transpone una matriz según el número de 
    filas y columnas proporcionadas por el usuario.
    
    Args:
        num_filas (int): Representa el número de filas en la matriz original.

        num_columnas (int): Representa el número de columnas en la matriz
        original. 

        filas (list): Almacenar las filas transpuestas de la matriz. 

        matriz (list): Es la matriz original que se va a trasponer.
    
    Returns:
        Se devuelve una matriz transpuesta basada en los parámetros de entrada
        y la matriz proporcionada.
    """
    
    # Se vacía la lista para no interferir en el proceso de la otra matriz
    filas = [] 
    print(f"La matriz traspuesta se ve de la siguiente forma:")

    # Se recorren la cantidad de filas ingresadas por el usuario
    for i in range(num_columnas): 

        # Se recorren la cantidad de columnas ingresadas por el usuario
        for j in range(num_filas):

        # Se ingresan las columnas como filas
            filas.append(matriz[j][i])

        # Se añade la fila a la matriz
        matriz_traspuesta.append(filas) 

        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")

        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_traspuesta

if __name__ == "__main__":
    # Solicitud: número de filas y columnas de la primera matriz
    num_filas = int(input("Ingrese número de filas"))
    num_columnas = int(input("Ingrese número de columnas"))

    # Condicional para input de matrices con orden cero
    if num_filas == 0 and num_columnas == 0:
        print("La primera matriz no tiene filas ni columnas :(")

    # Condicional para input de matrices con orden negativo
    elif num_filas < 0 or num_columnas < 0:
        print("Una cantidad negativa de columnas/filas no es permitida")
    
    else:
        # Llamado de función para llenar la primera matriz
        matriz = llenar_matriz(matriz, num_filas, num_columnas, filas)
        
        # Llamado de función para trasponer matriz
        matriz_traspuesta = trasponer_matriz(num_filas, num_columnas, filas, matriz)
