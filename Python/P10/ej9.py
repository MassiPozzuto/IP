"""
Juego de la Gallina

El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario; si alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un ”gallina”. Se hizo un torneo para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas. Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos!
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se devía, o nunca lo hace.
Se debe programar la función 'torneo de gallinas' que recibe un diccionario (donde las claves representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y devuelve un diccionario con los puntajes obtendidos por cada jugador.

    problema torneo_de_gallinas (in estrategias: dict<str, str>) : dict<str, Z> {
        requiere: {estrategias tiene por lo menos 2 elementos (jugadores).}
        requiere: {Las claves de estrategias tienen longitud mayor a 0.}
        requiere: {Los valores de estrategias sólo pueden ser los strs ”me desvío siempre” ó ”me la banco y no me desvío”.}
        asegura: {Las claves de res y las claves de estrategias son iguales.}
        asegura: {Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar el torneo, dado que jugó una vez contra cada otro jugador.}
    }
"""

def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    res:dict[str, int] = {}

    for participante_actual, estrategia_actual in estrategias.items():
        res[participante_actual] = 0
        participante_actual_agresivo:bool = estrategia_actual == 'me la banco y no me desvío'
        for participante_rival, estrategia_rival in estrategias.items():
            if participante_actual != participante_rival:
                if participante_actual_agresivo and estrategia_actual == estrategia_rival: # Se chocan
                    res[participante_actual] -= 5
                elif  participante_actual_agresivo and estrategia_actual != estrategia_rival: # Jugador rival se desvia
                    res[participante_actual] += 10
                elif not participante_actual_agresivo and estrategia_actual == estrategia_rival: # Ambos se desvian
                    res[participante_actual] -= 10
                else: # Jugador actual se desvia
                    res[participante_actual] -= 15

    return res

print(torneo_de_gallinas({
    "Pedro": "me desvío siempre",
    "Massi": "me la banco y no me desvío",
    "Fran": "me la banco y no me desvío",
    "Simon": "me desvío siempre",
    "Juan": "me desvío siempre"
}))
