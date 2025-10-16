"""
La notación polaca inversa, también conocida como notación postfix, es una forma de escribir expresiones matemáticas en la que los operadores siguen a sus operandos. Por ejemplo, la expresión “3 + 4” se escribe como “3 4 +” en notación postfix. Para evaluar una expresión en notación postfix, se puede usar una pila. Implementar una solución para el siguiente
problema.
    problema evaluar_expresion (in s: seq⟨Char⟩) : R {
        requiere: {s solo contiene números enteros y los operadores binarios +, -, * y /}
        requiere: {Todos los elementos (operandos y operadores) están separados por un único espacio}
        requiere: {La expresión es sintácticamente válida: cada operador binario tiene exactamente dos operandos previos disponibles en el momento de su evaluación.}
        asegura: {res es el valor obtenido al evaluar la expresión postfija representada por s}
    }

Para resolver este problema, se recomienda seguir el siguiente algoritmo:
    1. Dividir la expresión en tokens (operandos y operadores) utilizando espacios como delimitadores.
    2. Recorre los tokens uno por uno.
        a) Si es un operando, agrégalo a una pila.
        b) Si es un operador, saca los dos operandos superiores de la pila, aplicale el operador y luego coloca el resultado en la pila.
    3. Al final de la evaluación, la pila contendrá el resultado de la expresión.

Ejemplo de uso:
    expresion = "3 4 + 5 * 2 -"
    resultado = evaluar_expresion(expresion)
    print(resultado) # Debería imprimir 33
"""
from queue import LifoQueue as Pila        

def evaluar_expresion(expresion: str) -> float:
    operandos:Pila[int] = Pila()
    expresion_separada:list[str] = separar_string(expresion, ' ') # expresion.split()

    for elemento in expresion_separada:
        if elemento not in ['+', '-', '/', '*']:
            operandos.put(float(elemento))
        else:
            # Si la expresion esta bien formada, entonces si elemento es un operador, en la pila debe haber dos operandos
            operando2: float = operandos.get()
            operando1: float = operandos.get()
            operacion: str = f"{operando1} {elemento} {operando2}"
            operandos.put(eval(operacion)) # Como los operadores estan en formato string, existe una funcion en python que nos permite calcular una cuenta que esta en str
    
    # Si la expresion esta bien formada e hicimos todo bien, deberia quedarnos un solo elemento en la pila el cual es el resultado
    return operandos.get()


# Diria que hace casi lo mismo que .split()
def separar_string(string:str, separador:str = ' ') -> list[str]:
    if not separador: return string

    res:list[str] = []
    acumulador:str = ''
    for char in string:
        if char != separador:
            acumulador += char
        else:
            res.append(acumulador)
            acumulador = ''
    
    if len(acumulador) > 0: res.append(acumulador)
    
    return res
