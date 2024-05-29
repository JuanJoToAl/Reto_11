# Se declaran e inicializan las listas
matriz : list = []
filas : list = []

# Se declaran las variables
num_filas : int
num_columnas : int
columna : int
suma_columna : float

def llenar_matriz(matriz : list, num_filas : int, num_columnas : int, 
                  filas : list) -> list:
    """
    Esta función de Python llena una matriz con números ingresados 
    por el usuario.
    
    Args:
        matriz (list): Es una lista que almacenará los elementos de la 
        matriz que se está llenando.

        num_filas (int): Representa el número de filas en la matriz que 
        el usuario quiere crear.

        num_columnas (int): Representa el número de columnas en la matriz 
        que el usuario desea crear.

        filas (list): Es una lista que se utiliza para almacenar 
        los elementos de cada fila de la matriz. 
    
    Returns:
        Se devuelve la matriz llena como una lista.
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

def sumar_columnas(matriz : list, columna : int) -> list:
    """
    La función `sumar_columnas` toma una matriz y un índice de columna 
    como entrada, suma los elementos de esa columna y devuelve la suma.
    
    Args:
        matriz (list): Es una lista de listas. 
        
        columna (int): Representa el índice de la columna en 
        la matriz que desea sumar. 
    
    Returns:
        Se devuelve la suma de los elementos en la columna especificada 
        de la matriz de entrada.
    """
    
    # Se suman los elementos de la columna
    suma_columna = sum(matriz[i][columna - 1] for i in range(len(matriz)))

    # Se imprime la lista de elementos sumados
    columna = [matriz[i][columna - 1] for i in range(len(matriz))]
    print(f"Columna a sumar: {columna}")
    
    return suma_columna

if __name__ == "__main__":
    # Solicitud: número de filas y columnas de la primera matriz
    num_filas = int(input("Ingrese número de filas"))
    num_columnas = int(input("Ingrese número de columnas"))

    # Solicitud: columna para sumar
    columna = int(input("¿Qué columna quiere sumar?"))

    # Condicional para input de matrices con orden cero
    if num_filas == 0 and num_columnas == 0:
        print("La matriz no tiene filas ni columnas :(")

    # Condicional para input de matrices con orden negativo
    elif num_filas < 0 or num_columnas < 0:
        print("Una cantidad negativa de columnas/filas no es permitida")

    # Condicional para solicitud de columna fuera de rango
    elif num_columnas < columna:
        print(f"La matriz no tiene columna {columna}")
    else:

        # Llamado de función para llenar la primera matriz
        matriz = llenar_matriz(matriz, num_filas, num_columnas, filas)

        # Llamado de función para sumar columna
        suma_columna = sumar_columnas(matriz, columna)
        print(f"El resultado de la suma es: {suma_columna}")
