from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1 (2,25 puntos) -----------------------------------------------------------------
"""
Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
    requiere: { La longitud de v es distinto de 0 }
    asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
}

problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
    asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
}
"""
def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    subsecuencia_mas_larga: list[int] = [0]
    subsecuencia_actual: list[int] = [0]

    for i in range(len(v) - 1):
        if v[i + 1] != v[i] + 1 :
            if len(subsecuencia_actual) > len(subsecuencia_mas_larga):
                subsecuencia_mas_larga = subsecuencia_actual.copy()
            subsecuencia_actual = []
        subsecuencia_actual.append(i + 1)

    if len(subsecuencia_actual) > len(subsecuencia_mas_larga): # La subsecuencia mas larga esta en el final de la lista pasada
        subsecuencia_mas_larga = subsecuencia_actual.copy()

    return (len(subsecuencia_mas_larga), subsecuencia_mas_larga[0])


# Ejercicio 2 (2,25 puntos) -----------------------------------------------------------------
"""
Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana en una cola. En cada uno Ana respondió todas las preguntas.

problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
    requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
    asegura: { res tiene la misma cantidad de elementos que examenes }
    asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
}
"""
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    res:list[int] = []
    cola_aux:Cola[list[bool]] = Cola()

    while not examenes.empty():
        examen:list[bool] = examenes.get()
        cola_aux.put(examen)

        cant_True:int = 0
        cant_False:int = 0
        for respuesta in examen:
            if respuesta: cant_True += 1
            else: cant_False += 1
        
        cant_posibles_correctas:int = len(examen)
        if cant_True > cant_False:
            cant_posibles_correctas += int(len(examen) / 2) - cant_True
        elif cant_False > cant_True:
            cant_posibles_correctas += int(len(examen) / 2) - cant_False
        res.append(cant_posibles_correctas)
        
    while not cola_aux.empty():
        examenes.put(cola_aux.get())
    
    return res


# Ejercicio 3 (2,25 puntos) -----------------------------------------------------------------
"""
problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
    requiere: { Todas las filas de A tienen la misma longitud }
    requiere: { El mínimo número que aparece en A es igual a 1 }
    requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
    requiere: { No hay enteros repetidos en A }
    requiere: { Existen al menos dos enteros distintos en A }
    modifica: { A }
    asegura: { A tiene exactamente las mismas dimensiones que A@pre }
    asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
    asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
}
"""
def cambiar_matriz(A: list[list[int]]) -> None:
    elemento_anterior:int = A[len(A) - 1][len(A[0]) - 1]
    for i in range(len(A)):
        for j in range(len(A[0])):
            elemento_actual:int = A[i][j]
            A[i][j] = elemento_anterior
            elemento_anterior = elemento_actual


# Ejercicio 4 (2,25 puntos) -----------------------------------------------------------------
"""
Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
    requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
    asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
    asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
    asegura: { Los valores de res son positivos }
}
"""
def palabras_por_vocales(texto: str) -> dict[int, int]:
    res: dict[int, int] = {}

    vocales_palabra_actual:int = 0
    for letra in texto:
        if letra in ['A','a','E','e','I','i','O','o','U','u']:
            vocales_palabra_actual += 1
        elif letra == ' ' and vocales_palabra_actual != 0:
            if vocales_palabra_actual not in res.keys():
                res[vocales_palabra_actual] = 1
            else:
                res[vocales_palabra_actual] += 1
            
            vocales_palabra_actual = 0

    if vocales_palabra_actual not in res.keys() and vocales_palabra_actual != 0:
        res[vocales_palabra_actual] = 1
    elif vocales_palabra_actual != 0:
        res[vocales_palabra_actual] += 1

    return res


# Ejercicio 5 (1 puntos) --------------------------------------------------------------------
"""
¿Por qué en Paradigma Imperativo no existe la transparencia referencial?
    [ ] Utilizamos otro mecanismo de repetición de código, en lugar de recursión usamos la iteración (FOR, WHILE, DO WHILE).
    [X] Tenemos una nueva instrucción, la asignación, que nos permite cambiar el valor de una variable
    [ ] El orden en que se ejecutan las instrucciones del programa es diferente
"""