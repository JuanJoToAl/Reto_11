# Reto_11
"El siguiente repositorio contiene propuestas de solución a los puntos del reto 11"

### 1. Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

### 2. Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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



def llenar_matriz_primera(matriz_primera : list, num_filas_primera : int, 
                          num_columnas_primera : int, filas : list) -> list:

    print(f"La primera matriz se ve de la siguiente forma:")
    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas_primera): 
        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas_primera):
        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(f"Primera matriz: ingrese un número ({i + 1}, {j + 1})")))
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
            filas.append(float(input((f"Segunda matriz: ingrese un número ({i + 1}, {j + 1})"))))
        # Se añade la fila a la matriz
        matriz_segunda.append(filas) 
        # Se imprime la fila para ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")
        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz_segunda

def multiplicar_matrices(matriz_primera, matriz_segunda, 
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
            # Se multiplica una fila por las columnas
            multiplicacion_elemento = sum(filas[i] * columnas[i] for i in range(len(filas)))
            # Se almacena el resultado en la lista
            multiplicacion_final.append(multiplicacion_elemento)
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
```

### 3. Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

### 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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

    print(f"La matriz se ve de la siguiente forma:")
    # Se recorre la cantidad de filas ingresadas por el usuario
    for i in range(num_filas): 
        # Se recorre la cantidad de columnas ingresadas por el usuario
        for j in range(num_columnas):
        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input(f"Primera matriz: ingrese un número ({i + 1}, {j + 1})")))
        # Se añade la fila a la matriz
        matriz.append(filas) 
        # Se imprime la fila ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")
        # Se vacía variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz

def sumar_columnas(matriz : list, columna : int) -> list:
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
```

### 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
# Se declaran e inicializan las listas
matriz : list = []
filas : list = []
# Se declaran las variables
num_filas : int
num_columnas : int
fila : int
suma_fila : float

def llenar_matriz(matriz : list, num_filas : int, num_columnas : int, 
                  filas : list) -> list:

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

def sumar_filas(matriz : list, fila : int) -> list:
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
```
