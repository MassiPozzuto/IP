# Implementar las siguientes funciones usando repetición condicional while:

# 1. Escribir una función que imprima los números del 1 al 10
def del_1_al_10()-> None:
    i:int = 1
    while(i < 11):
        print(i)
        i+=1

# 2. Escribir una función que imprima los números pares entre el 10 y el 40.
def pares_entre_10_y_40()-> None:
    i:int = 10
    while(i < 41):
        print(i)
        i+=2

# 3. Escribir una función que imprima la palabra "eco" 10 veces.
def eco_10_veces()-> None:
    i:int = 1
    while(i < 11):
        print("eco")
        i+=1

# 4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último "Despegue".
def despegue(cuenta_regresiva:int)-> None:
    while (cuenta_regresiva > 0):
        print(cuenta_regresiva)
        cuenta_regresiva -= 1
    print("Despegue")

# 5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, "el año de partida" y "algún año de llegada", siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos de un año y la función debe mostrar el texto: "Viajó un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de año.
def viaje_al_pasado(partida:int, llegada:int):
    while (partida > llegada):
        partida -= 1
        print(f"Viajó un año al pasado, estamos en el año: {partida}")

# 6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, vamos a viajar de a 20 años en cada salto!
def viaje_al_pasado2(partida:int):
    while (partida >= -364):
        partida -= 20
        print(f"Viajó 20 años al pasado, estamos en el año: {partida if (partida >= 0) else f"{abs(partida)} a.C"}")
