# Se declaran e inicializan las listas
matriz : list = []
filas : list = []

# Se declaran las variables
num_filas : int
num_columnas : int
fila : int
suma_fila : float

def llenar_matriz(matriz : list, num_filas : int, 
                  num_columnas : int, filas : list) -> list:
    """
    La función `llenar_matriz` toma la entrada del usuario para llenar 
    una matriz con un número específico de filas y columnas.
    
    Args:
        matriz (list): Es una lista que almacenará los elementos de la 
        matriz que se está llenando.

        num_filas (int): Representa el número de filas en la matriz que el
        usuario quiere crear. 

        num_columnas (int): Representa el número de columnas en la matriz que
        el usuario desea crear. 

        filas (list): Es una lista que se utiliza para almacenar los elementos 
        de cada fila de la matriz. 
    
    Returns:
        Se devuelve la matriz llena como una lista después de que el 
        usuario haya ingresado los números para cada celda de la matriz.
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

def sumar_filas(matriz : list, fila : int) -> list:
    """
    La función toma una matriz y un índice de fila como entrada, 
    suma los elementos en la fila especificada y devuelve la suma.
    
    Args:
        matriz (list): Es una lista de listas que representa una matriz. 

        fila (int): Representa el índice de la fila en la matriz 
        que deseas sumar. 
    
    Returns:
      Se devuelve la suma de los elementos en la fila especificada de la matriz.
    """

    # Se suman los elementos de la fila
    suma_fila = sum(matriz[fila - 1][j] for j in range(len(matriz)))

    # Se imprime la lista de elementos sumados
    fila = [matriz[fila - 1][j] for j in range(len(matriz))]
    print(f"Fila a sumar: {fila}")
    
    return suma_fila

if __name__ == "__main__":
    # Solicitud: número de filas y columnas de la primera matriz
    num_filas = int(input("Ingrese número de filas"))
    num_columnas = int(input("Ingrese número de columnas"))

    # Solicitud: columna para sumar
    fila = int(input("¿Qué fila quiere sumar?"))

    # Condicional para input de matrices con orden cero
    if num_filas == 0 and num_columnas == 0:
        print("La matriz no tiene filas ni columnas :(")

    # Condicional para input de matrices con orden negativo
    elif num_filas < 0 or num_columnas < 0:
        print("Una cantidad negativa de columnas/filas no es permitida")

    # Condicional para solicitud de fila fuera de rango
    elif num_filas < fila:
        print(f"La matriz no tiene fila {fila}")
    else:

        # Llamado de función para llenar la primera matriz
        matriz = llenar_matriz(matriz, num_filas, num_columnas, filas)

        # Llamado de función para sumar fila
        suma_fila = sumar_filas(matriz, fila)
        print(f"El resultado de la suma es: {suma_fila}")
