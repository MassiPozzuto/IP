def  alguno_es_0(numero1: float, numero2: float) -> bool:
    res:bool = numero1 == 0 or numero2 == 0
    return res

def  ambos_son_0(numero1: float, numero2: float) -> bool:
    res:bool = numero1 == 0 and numero2 == 0
    return res

def es_nombre_largo(nombre: str) -> bool:
    res:bool = len(nombre) > 2 and len(nombre) < 9
    return res

def es_bisiesto(anio: int) -> bool:
    res:bool = (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0 )
    return res