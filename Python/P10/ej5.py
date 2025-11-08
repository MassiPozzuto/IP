"""
Sala de Escape - Promedio de salidas

Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de una habitación resolviendo enigmas, llevan un registro meticuloso de todas las salas de escape que hay en Capital. Este registro indica si han visitado una sala y si pudieron o no salir de ella. Un 0 significa que no fueron, un 61 que no lograron salir a tiempo, y un número entre 1 y 60 representa los minutos que les tomó escapar exitosamente. Con estos datos, pueden comparar sus logros y desafíos en cada nueva aventura que emprenden juntos.

Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados para cada sala de escape en Capital, escribir una función en Python que devuelva un diccionario. En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir).

    problema promedio_de_salidas (in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z×R>> {
        requiere: {registro tiene por lo menos un integrante.}
        requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
        requiere: {Todos los valores de registro tiene la misma longitud.}
        requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive.}
        asegura: {res tiene las mismas claves que registro.}
        asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro.}
        asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0.}
    }
"""

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res:dict[str, tuple[int, float]] = {}

    for amigo, tiempos in registro.items():
        suma_tiempo_salidas:int = 0
        cant_salidas:int = 0

        for tiempo in tiempos:
            if tiempo > 0 and tiempo < 61:
                cant_salidas += 1
                suma_tiempo_salidas += tiempo
        
        res[amigo] = (cant_salidas, suma_tiempo_salidas / cant_salidas) # Como registro es un diccionario, las claves son unicas, no hace falta verificar si existen en res
    
    return res