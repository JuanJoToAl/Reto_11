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
producto_elemento : float



def llenar_matriz_primera(matriz_primera : list, num_filas_primera : int, num_columnas_primera : int, filas : list) -> list:
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

def llenar_matriz(matriz : list, num_filas : int, num_columnas : int, filas : list) -> list:
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
```
