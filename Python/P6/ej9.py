"""
Sea el siguiente código:

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g
    
g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

"""

# 1. Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# ===> 1st: ro(1) = 2
# ===> 2nd: ro(1) = 3
# ===> 3rd: ro(1) = 4

# 2. Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# ===> 1st: rt(1, 0) = 2
# ===> 2nd: rt(1, 0) = 2
# ===> 3rd: rt(1, 0) = 2

# 3. En cada función, realizar la ejecución simbólica.
"""
def rt(x: int, g: int) -> int:
        // Estado a
    g = g + 1
        // Estado b
        // Vale g == g@a + 1
    return x + g

g: int = 0
    // Estado a
def ro(x: int) -> int:
    global g
        // Estado b
    g = g + 1
        // Estado c
        // Vale g == g@b + 1
    return x + g
"""

# 4. Dar la especificación para cada función, rt y ro.
"""
problema rt(in x:Z, in g:Z) -> Z {
    require: { True }
    modifica: g
    asegura: { res = x + (g + 1) }
}

problema rt(in x:Z, inout g:Z) -> Z {
    require: { True }
    modifica: g
    asegura: { res = x + (g@pre + 1) }
}

"""