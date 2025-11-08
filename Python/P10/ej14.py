"""
Hospital - Alarma epidemiológica

Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

    problema alarma_epidemiologica (in registros : seq⟨Z × str⟩, in infecciosas : seq⟨str⟩, in umbral : R) : dict<str, R> {
        requiere: {0 < umbral < 1.}
        asegura: {claves de res pertenecen a infecciosas.}
        asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
        asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
    }
"""

def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    pacientes_enfermos_de_infecciosas: dict[str, int] = {}
    for _, enfermedad in registros:
        if enfermedad not in pacientes_enfermos_de_infecciosas.keys() and enfermedad in infecciosas:
            pacientes_enfermos_de_infecciosas[enfermedad] = 1
        elif enfermedad in infecciosas:
            pacientes_enfermos_de_infecciosas[enfermedad] += 1

    res: dict[str, float] = {}
    total_pacientes:int = len(registros)    
    for enfermedad_infecciosa, cant_infectados in pacientes_enfermos_de_infecciosas.items():
        proporcion_infectados :float = cant_infectados / total_pacientes
        if proporcion_infectados >= umbral:
            res[enfermedad_infecciosa] = proporcion_infectados

    return res
