{-
a) Implementar la funcion:
    distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float

    problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
        requiere: {True}
        asegura: {res = La serie que va de i=0 a 2 de |pi − qi|}
    }

Por ejemplo:
    distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
    distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8

b) Reimplementar la funcion teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
-}

type Punto3D = (Float, Float, Float)

distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (x, y, z) (a, b, c) = abs (x - a) + abs (y - b) + abs (z - c)