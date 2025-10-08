import math

# a)
def imprimir_hola_mundo() -> None :
    print("Hola mundo!")

# b)
def imprimir_un_tema() -> None:
    print("""
        Mira lo que se avecina
        Si el domingo las gallinas
        No le ganan a belgrano.
        pierden la categoria
        Los esperaran los hinchas
        Y a roman van a colgarlo
          
        Si le ganan los piratas
        Jugaran con los canallas
        Y visitaran en san martin a chaca
        Si la zona no conocen
        Le va a regalar la 12
        Un gps para llegar a la cancha
        La de Merlo, de Defensa, y Atlanta
          
        Se va a la B, ya, riber
        Juega con Patronato, Ferro, Quilmes
        Y el Boca de Corrientes que habla en Guarani
        Se va al a B, ya, riber
        Juega contra Almirante, Instituto, Defensa y Justicia
        Y en Tucuman, San Martin.
        Se va al a B, ya, riber
        Esta en Jujuy Gimnasia,
        El globito, termina en Mar del Plata contra Aldosiví 
        (x2) 
    """)

# c)
def raizDe2() -> float:
    res:float = round(math.sqrt(2), 4)
    return res

# d)
def factorial_de_dos() -> int :
    res:int = 2 * 1
    return res

# e)
def perimetro() -> float:
    res:float = 2 * math.pi
    return res
