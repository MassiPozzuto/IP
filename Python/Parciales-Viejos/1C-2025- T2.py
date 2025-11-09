from queue import Queue as Cola

# Ejercicio 1
def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    res:int = 0
    
    for i in range(len(s) - 1):
        for j in range(len(s)):
            if i < j and s[i] + s[j] == n:
                res += 1
                
    return res



# Ejercicio 2 
def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    res:str = ""
    clientes_final:Cola[tuple[str, str, int]] = Cola()
    
    while not clientes.empty():
        cliente_actual:tuple[str, str, int] = clientes.get()
        if cliente_actual[1] != "efectivo" and cliente_actual[2] <= 15 and res == "":
            res = cliente_actual[0]
        else:
            clientes_final.put(cliente_actual)
    
    while not clientes_final.empty():
        clientes.put(clientes_final.get())
    
    return res



# Ejercicio 3 
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    A_copia:list[list[int]] = deep_copy(A)
    
    for i in range(len(A)):
        A[i][col1] = A_copia[len(A)-1-i][col2]
        A[i][col2] = A_copia[len(A)-1-i][col1]
            
    return

def deep_copy(matriz:list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    
    fila_aux:list[int] = []
    for fila in matriz:
        for col in fila:
            fila_aux.append(col)
        res.append(fila_aux)
        fila_aux = []

    return res



# Ejercicio 4
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    res:dict[str, int] = {}
    
    for persona, localidad in censo1.items():
        if censo1[persona] == censo2[persona]:
            if localidad not in res.keys():
                res[localidad] = 0
            res[localidad] += 1
        
    return res