# Implementar los siguientes problemas de alternativa condicional (if/else). Los enunciados pueden no ser del todo claros, especificar los problemas en nuestro lenguaje de especificación y programar en base a tu propuesta de especificación.

# 1. devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en caso contrario.
def devolver_el_doble_si_es_par(num: int) -> int:
    res:int = (num * 2) if (num % 2 == 0) else num
    return res

# 2. devolver_valor_si_es_par_sino_el_que_sigue(numero); que devuelve el mismo número si es par y sino el siguiente.
# Analizar distintas formas de implementación (usando un if-then-else, y 2 if), todas funcionan?
def devolver_valor_si_es_par_sino_el_que_sigue(num: int) -> int:
    res:int = num if (num % 2 == 0) else (num + 1)
    return res

# 3. devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero). En otro caso devolver el número original. 
# Analizar distintas formas de implementación (usando un if-then-else, y 2 if, usando alguna opción de operación lógica), todas funcionan? Cuál es el resultado si la entrada es 18?
"""
problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: Z): Z {
    requiere: { True }
    asegura: { res = 3n <=> n es multiplo de 9 }
    asegura: { res = 2n <=> n es multiplo de 3 pero no de 9 }
    asegura: { res = n <=> n no es multiplo de 3 ni multiplo de 9 }
}
"""
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(num: int) -> int:
    if (num % 9 == 0):
        num *= 3
    elif (num % 3 == 0):
        num *= 2

    return num 

# 4. lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga "Tu nombre tiene muchas letras!" y sino, "Tu nombre tiene menos de 5 caracteres".
def lindo_nombre(nombre: str) -> str :
    res:str = "Tu nombre tiene muchas letras!" if (len(nombre) >= 5) else "Tu nombre tiene menos de 5 caracteres"
    return res

# 5. elRango(numero) que imprime por pantalla "Menor a 5" si el número es menor a 5, "Entre 10 y 20" si el número está en ese rango y "Mayor a 20" si el número es mayor a 20.
def elRango(numero: float) -> None:
    if numero < 5:
        print("Menor a 5")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")
    else:
        print("Tu numero no se encuentra en ningun rango")

# 6. En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de las personas se les ordena ir a trabajar. 
# Implemente una función que, dados los parámetros de sexo (F o M) y edad, imprima la frase que corresponda según el caso: "Andá de vacaciones" o "Te toca trabajar".
def vacacionbes_o_trabajo(sexo:chr, edad:int) -> None:
    if edad < 18 or (sexo == 'F' and edad >= 60) or (sexo == 'M' and edad >= 65):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")