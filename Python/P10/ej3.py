"""
Veterinaria - Flujo de pacientes

Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una función en Python que encuentre la secuencia más larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
Se pide implementar una función que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el índice donde comienza la subsecuencia más larga que cumpla con estas condiciones.

    problema subsecuencia_mas_larga (in tipos_pacientes_atendidos : seq⟨str⟩) : Z {
        requiere: {tipos_pacientes_atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
        asegura: {res es el índice donde empieza la subsecuencia más larga de tipos_pacientes_atendidos que contenga solo elementos ”perro” o ”gato”.}
        asegura: {Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera.}
    }
"""

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    subsecuencia_mas_larga:tuple = (0, 0)

    subsecuencia_actual:list[str] = []
    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == 'perro' or tipos_pacientes_atendidos[i] == 'gato':
            subsecuencia_actual.append(i)
        else:
            if len(subsecuencia_actual) > subsecuencia_mas_larga[1]:
                subsecuencia_mas_larga = (i - len(subsecuencia_actual), len(subsecuencia_actual))
            subsecuencia_actual.clear()
    
    if len(subsecuencia_actual) > subsecuencia_mas_larga[1]:
        indice_subsecuencia:int = len(tipos_pacientes_atendidos) - len(subsecuencia_actual)
        subsecuencia_mas_larga = (indice_subsecuencia, len(subsecuencia_actual))

    return subsecuencia_mas_larga[0]

print(subsecuencia_mas_larga(["perro", "gato", "caballo", "perro", "gato","perro", "caballo","perro", "caballo", "perro", "gato", "perro"]))