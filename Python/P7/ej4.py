"""
Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento "I" para ingreso de dinero y "R" para retiro de dinero, y además el monto de cada operación. Por ejemplo, si la lista de tuplas es [("I", 2000), ("R", 20),("R", 1000),("I", 300)] entonces el saldo actual es 1280.

Ver especificación en el apunte
"""

def saldo_actual(movimientos:list[tuple[str, int]]) -> int:
    saldo:int = 0
    for movimiento in movimientos:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    
    return saldo
