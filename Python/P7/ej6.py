from ej1 import ordenados
import numpy as np 
# Implementar las siguientes funciones sobre matrices (secuencias de secuencias):

"""
1. 
    problema es_matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
        requiere: { T rue }
        asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
    }
"""
def es_matriz(lista_bidimensional:list[list[int]]) -> bool:
    res:bool = True if (len(lista_bidimensional) > 0 and len(lista_bidimensional[0])) > 0  else False
    for fila in lista_bidimensional:
        if len(fila) != len(lista_bidimensional[0]):
            res = False
    return res

"""
2. 
    problema filas_ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
        requiere: { es_matriz(m) }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
    }
Nota: Reutilizar la función ordenados() implementada previamente para listas
"""
def filas_ordenadas(matriz:list[list[int]]) -> list[bool]:
    res:bool = True
    for fila in matriz:
        if not ordenados(fila): # Importada de ej1.py
            res = False
            break
    return res

"""
3. 
    problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
        requiere: { es_matriz(m) }
        requiere: { c < |m[0]| }
        requiere: { c ≥ 0 }
        asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en el mismo orden que aparecen }
    }
"""
def columna(matriz:list[list[int]], col:int) -> list[int]:
    res:list[int] = []
    for fila in matriz:
        res.append(fila[col])
    return res

"""
4. 
    problema columnas_ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
        requiere: { es_matriz(m) }
        asegura: { Para todo índice de columna c: 0 ≤ c < |m[0]| → (res[c] = true ↔ ordenados(columna(m, c))) }
        asegura: {|res| = |m[0]|}
    }
Nota: Reutilizar la función ordenados() implementada previamente para listas
"""
def columnas_ordenadas(matriz:list[list[int]]) -> list[bool]:
    res:list[bool] = []
    for c in range(len(matriz[0])):
        res.append(ordenados(columna(matriz, c)))
    return res

"""
5. 
    problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
        requiere: { es_matriz(m) }
        asegura: { Devuelve mt (o sea la matriz transpuesta) }
    }
Nota: Usar columna() para ir obteniendo todas las columnas de la matriz.
"""
def transponer(matriz:list[list[int]]) -> list[list[int]]:
    res:list[list[int]] = []
    for c in range(len(matriz[0])):
        res.append(columna(matriz, c))
    return res

"""
6. Ta-Te-Ti Tradicional:
    problema quien_gana_tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
        requiere: { es_matriz(m) }
        requiere: { |m| = 3 }
        requiere: { |m[0]| = 3 }
        requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
        requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
        requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
        requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
        requiere: { Para todo i,j ∈ {0, 1, 2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = " "}
        asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
        asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
        asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
    }
"""
def quien_gana_tateti(tablero:list[list[str]]) -> int:
    ganador:int = 2
    
    # Ganador horizontal
    for fila in tablero:
        if fila[0] != ' ' and fila[0] == fila[1] and fila[0] == fila[2]:
            ganador = 1 if fila[0] == 'X' else 0
    
    # Ganador vertical
    for columna in transponer(tablero):
        if columna[0] != ' ' and columna[0] == columna[1] and columna[0] == columna[2]:
            ganador = 1 if columna[0] == 'X' else 0

    # Ganador diagonal
    mismos_elementos_diagonal_der:bool = tablero[1][1] == tablero[0][0] and tablero[1][1] == tablero[2][2]
    mismos_elementos_diagonal_izq:bool = tablero[1][1] == tablero[0][2] and tablero[1][1] == tablero[2][0]
    if tablero[1][1] != ' ' and (mismos_elementos_diagonal_der or mismos_elementos_diagonal_izq):
        ganador = 1 if tablero[1][1] == 'X' else 0
    
    return ganador


"""
7. Opcional: Implementar una función que tome un entero d y otro p y eleve una matriz cuadrada de tamaño d con valores generados al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por sí misma p veces. Realizar experimentos con diferentes valores de d. ¿Qué pasa con valores muy grandes?
    problema exponenciacion_matriz (in d:Z, in p:Z) : seq⟨seq⟨Z⟩⟩ {
        requiere: { d, p ∈ Z y d, p > 0 }
        asegura: { es_matriz(m) y |columna(m, 0)| = d y |columna(transponer(m), 0)| = d y res = productoria desde i=1 hasta p de m }
    }

Nota 1: 
    recordá que en la multiplicación de una matriz cuadrada de dimensión d por si misma cada posición se calcula como res[i][j] = Pd-1 k=0(m[i][k] × m[k][j])
Nota 2: 
    para generar una matriz cuadrada de dimensión d con valores aleatorios hay muchas opciones de implementación, analizar las siguientes usando la biblioteca numpy 

Opción 1:
    import numpy as np
    m = np.random.random((d, d))
Opción 2:
    import numpy as np
    m = np.random.randint(i,f, (d, d))
"""
# Mejor saltear, la aprte de ramdomizar los numeros de la matriz lo unico que hace es perder seguimiento de lo que hacemos. Si fuese con matrices conocidas quizas aporte un mejor aprendizaje


# La opcion 1: Genera una matriz de d*d con valores float random entre 0 y 1 (floats)
# La opcion 2: Genera una matriz de d*d con valores int random entre i y f
# Ambas matrices son matrices de arrays no de listas
def exponenciacion_matriz_random(d:int, p:int) -> list[list[int]]:
    matriz_original:list[list[int]] = np.random.randint(0,100, (d, d)).tolist() # Estoy limitando los numeros random arbitrariamente a estar entre 0 y 100
    matriz_exponenciada:list[list[int]] = exponenciacion_matriz(matriz_original, p)
    return matriz_exponenciada

def exponenciacion_matriz(matriz:list[list[int]], p:int) -> list[list[int]]:
    matriz_exponenciada:list[list[int]] = matriz.copy()
    while p > 1:
        matriz_exponenciada = multiplicar_matrices(matriz_exponenciada, matriz)
        p -= 1
    return matriz_exponenciada

def multiplicar_matrices(m1:list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    n_filas = len(m1)
    n_columnas = len(m2[0])
    # Inicializar matriz default
    nueva_matriz = [[0] * n_columnas for _ in range(n_filas)]

    for i in range(n_filas):
        for r in range(n_columnas):
            nueva_matriz[i][r] = multiplicar_listas(m1[i], columna(m2, r))

    return nueva_matriz

def multiplicar_listas(l1:list[int], l2:list[int]) -> int:
    res:int = 0
    for i in range(len(l1)):
        res += l1[i] * l2[i]
    return res


print(exponenciacion_matriz_random(3, 2))
print('---')
print(exponenciacion_matriz_random(5, 2))
print('---')
print(exponenciacion_matriz_random(10, 2))
print('---')
print(exponenciacion_matriz_random(15, 2))

# Observemos que cuanto mas grande d, mas grande es la matriz, pues d representa la cantidad de filas y columnas. Ademas los numeros tambien tienden a ser mas grande ya que al realizar la potencia involucramos mas sumas y multiplicaciones
