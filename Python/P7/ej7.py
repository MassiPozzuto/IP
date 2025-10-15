import random
#Vamos a elaborar programas interactivos (usando la función input()) que nos permita solicitar al usuario información cuando usamos las funciones.

"""
1. Implementar una función para construir una lista con los nombres de mis estudiantes. La función solicitará al usuario los nombres hasta que ingrese la palabra “listo”, o vacío (el usuario aprieta ENTER sin escribir nada). Devuelve la lista con todos los nombres ingresados.
"""
def ingresar_estudiantes() -> list[str]:
    lista_estudiantes:list[str] = []
    estado:bool = True
    while estado:
        str_ingresado = input("Ingrese un estudiante o 'listo' para finalizar: ")
        if not str_ingresado or str_ingresado == "listo":
            estado = False
        else:
            lista_estudiantes.append(str_ingresado)
    return lista_estudiantes

"""
2. Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE).
El usuario debe seleccionar en cada paso si quiere:
    - “C” = Cargar créditos,
    - “D” = Descontar créditos,
    - “X” = Finalizar la simulación (terminar el programa).
En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a asumir que el monedero comienza en cero. Para guardar la información grabaremos en el historial tuplas que representen los casos de cargar (“C”, monto a cargar) y descontar crédito (“D”, monto a descontar).
"""
def monedero_electronico() -> list[tuple[str, int]]:
    historial:list[tuple[str, int]] = []
    saldo:int = 0 # Pongo el saldo, pero ni siquiera pide algo sobre esto. Podria pedir que el saldo no sea negativo

    estado:bool = True
    while estado:
        accion:str = input("Ingrese la accion a realizar ('C', 'D' o 'X'): ")
        if accion in ['C', 'D']:
            monto:int = int(input("Ingrese el monto entero deseado: ")) # Deberia tener en cuenta si el usuario ingresa algo que no es casteable a int
            if accion == 'C': saldo += monto
            else: saldo -= monto
            historial.append((accion, monto))
        else: estado = False

    print(f"Saldo final: {saldo}")
    return historial

"""
3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deberá generar un número aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deberá luego preguntarle al usuario si desea seguir sacando otra “carta” o plantarse. En este último caso el programa debe terminar. Los números aleatorios obtenidos deberán sumarse según el número obtenido salvo por las “figuras” (10, 11 y 12) que sumarán medio punto cada una. El programa debe ir acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la función devuelve el historial de “cartas” que hizo que el usuario gane o pierda. Para generar números pseudo-aleatorios entre 1 y 12 utilizaremos la función random.randint(1,12). Al mismo tiempo, la función random.choice() puede ser de gran ayuda a la hora de repartir cartas.
"""
def siete_y_medio() -> list[int]:
    print("Comienza el juego!")
    puntaje:float = 0
    historial_cartas:list[int] = []

    estado:bool = True
    while estado:
        nueva_carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        historial_cartas.append(nueva_carta)
        
        if nueva_carta in [10, 11, 12]: puntaje += 0.5
        else: puntaje += nueva_carta

        print(f"Sacaste un {nueva_carta}. Tu puntaje ahora es de: {puntaje}")
        if puntaje >= 7.5: 
            print("Oh no, te pasaste ;(")
            estado = False
        else: estado = input("Desea sacar otra carta o plantarse (c/p)?: ") == 'c'        

    print("Fin del juego!")
    print(f"Puntaje final: {puntaje}, {'perdiste :(' if puntaje >= 7.5 else 'ganaste!'}")
    return historial_cartas

"""
4. Analizar la fortaleza de una contraseña. Solicitar al usuario que ingrese un texto que será su contraseña. Armar una función que tenga de parámetro de entrada un string con la contraseña a analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “ñ/N” es considerado un carácter especial y no se comporta como cualquier otra letra. String es seq⟨Char⟩. Consejo: para ver si una letra es mayúscula se puede ver si está ordenada entre A y Z.
    - La contraseña será VERDE si:
        a) la longitud es mayor a 8 caracteres
        b) tiene al menos 1 letra minúscula.
        c) tiene al menos 1 letra mayúscula.
        d) tiene al menos 1 dígito numérico (0..9)
    - La contraseña será ROJA si:
        a) la longitud es menor a 5 caracteres.
    - En caso contrario será AMARILLA.

"""
def fortaleza_password(password: str) -> str:
    res:str = "AMARILLA"
    if len(password) < 5: 
        res = "ROJA"
    elif len(password) > 8 and contiene_mayus(password) and contiene_minus(password) and contiene_num(password):
        res = "VERDE"
    return res

def contiene_mayus(string:str) -> bool:
    res:bool = False
    for letra in string:
        if letra >= 'A' and letra <= 'Z':
            res = True
            break
    return res

def contiene_minus(string:str) -> bool:
    res:bool = False
    for letra in string:
        if letra >= 'a' and letra <= 'z':
            res = True
            break
    return res
    
def contiene_num(string:str) -> bool:
    res:bool = False
    for letra in string:
        if letra >= '0' and letra <= '9':
            res = True
            break
    return res
