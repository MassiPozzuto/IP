# Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la función range para generar una secuencia de números en un rango dado, con un valor inicial i, un valor final f y un paso p. Ver documentación: https://docs.python.org/es/3/library/stdtypes.html#typesseq-range
# 1. Escribir una función que imprima los números del 1 al 10
def del_1_al_10()-> None:
    for i in range(1,11,1):
        print(i)

# 2. Escribir una función que imprima los números pares entre el 10 y el 40.
def pares_entre_10_y_40()-> None:
    for i in range(10,41,2):
        print(i)

# 3. Escribir una función que imprima la palabra "eco" 10 veces.
def eco_10_veces()-> None:
    for _ in range(1,11,1):
        print("eco")

# 4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último "Despegue".
def despegue(inicio:int)-> None:
    for i in range(inicio, 0,-1):
        print(i)
    print("Despegue")

# 5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, "el año de partida" y "algún año de llegada", siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos de un año y la función debe mostrar el texto: "Viajó un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de año.
def viaje_al_pasado(partida:int, llegada:int):
    for anio in range(partida, llegada-1,-1):
        print(f"Viajó un año al pasado, estamos en el año: {anio}")


# 6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, vamos a viajar de a 20 años en cada salto!
def viaje_al_pasado2(partida:int):
    for anio in range(partida, -384,-20):
        print(f"Viajó 20 años al pasado, estamos en el año: {anio if (anio >= 0) else f"{abs(anio)} a.C"}")