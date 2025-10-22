"""
Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados para cada sala de escape en Capital, escribir una función en Python que devuelva un diccionario.
    problema promedio_de_salidas (in registro: dict[str, seq⟨Z⟩]) : dict[str, Z × R] {
        requiere: {registro tiene por lo menos un integrante.}
        requiere: {Todos los integrantes de registro tienen por lo menos un tiempo.}
        requiere: {Todos los valores de registro tienen la misma longitud.}
        requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive.}
        asegura: {res tiene exactamente las mismas claves que registro.}
        asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro.}
        asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0.}
    }
Ejemplo: dada la entrada {“a”:[61,60,59,58], “b”:[1,2,3,0] }, la salida es {“a”:(3, 59.0), “b”:(3, 2.0)}.
"""

def promedio_de_salidas(registro:dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res:dict[str, tuple[int, float]] = {}

    suma_tiempo:int = 0
    cantidad_de_salas_en_el_rango:int = 0
    promedio_tiempo_en_salas:float = 0.0
    for amigo, tiempos in registro.items():
        for tiempo in tiempos:
            if tiempo > 0 and tiempo < 61:
                suma_tiempo += tiempo
                cantidad_de_salas_en_el_rango += 1

        if cantidad_de_salas_en_el_rango > 0:
            promedio_tiempo_en_salas = suma_tiempo / cantidad_de_salas_en_el_rango
            res[amigo] = (cantidad_de_salas_en_el_rango, promedio_tiempo_en_salas)
        else:
            res[amigo] = (0, 0.0)

        suma_tiempo = 0
        cantidad_de_salas_en_el_rango = 0

    return res