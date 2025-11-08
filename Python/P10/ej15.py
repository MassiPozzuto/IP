"""
Hospital - Empleado del mes

Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

    problema empleados_del_mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: {No hay valores en horas que sean listas vacías.}
        asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
        asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs.}
        asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertenece a res.}
    }
"""

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
    empleados_del_mes: list[int] = []

    maximo_horas_trabajadas:int = 0
    horas_totales: dict[int, list[int]] = {}
    for id_empleado, horas_por_dia in horas.items():
        suma_horas_trabajadas_empleado:int = 0
        for hora in horas_por_dia:
            suma_horas_trabajadas_empleado += hora
        
        if suma_horas_trabajadas_empleado > maximo_horas_trabajadas:
            maximo_horas_trabajadas = suma_horas_trabajadas_empleado
        horas_totales[id_empleado] = suma_horas_trabajadas_empleado

    for id_empleado, horas_totales_empleado in horas_totales.items():
        if horas_totales_empleado == maximo_horas_trabajadas:
            empleados_del_mes.append(id_empleado)

    return empleados_del_mes