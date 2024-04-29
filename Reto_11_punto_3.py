# Se declaran e inicializan las listas
matriz : list = []
matriz_traspuesta : list = []
filas : list = []
# Se declaran las variables
num_filas : int
num_columnas : int

def llenar_matriz(matriz : list, num_filas : int, 
                          num_columnas : int, filas : list) -> list:

    print(f"La matriz se ve de la siguiente forma:")
    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas): 
        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas):
        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(f"Ingrese un número ({i + 1}, {j + 1})")))
        # Se añade la fila a la matriz
        matriz.append(filas) 
        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")
        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz

def trasponer_matriz(num_filas : int, num_columnas : int, 
                     filas : list, matriz : list) -> list:
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
