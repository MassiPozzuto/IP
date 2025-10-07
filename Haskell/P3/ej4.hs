-- Especificar e implementar las siguientes funciones utilizando tuplas para representar pares y ternas de numeros.

-- a) productoInterno: calcula el producto interno entre dos tuplas de R × R.
{-
    problema productoInterno ((a, b) : R × R, (c, d) : R × R): R {
        requiere: { True }
        asegura: { res = a × c + b × d }
    }
-}
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (a, b) (c, d) = a * c + b * d

-- b) esParMenor: dadas dos tuplas de R × R, decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla.
{-
    problema esParMenor ((a, b) : R × R, (c, d) : R × R): Bool {
        requiere: { True }
        asegura: { res = (a < c) ∧ (b < d) }
    }
-}
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (a, b) (c, d) = a < c && b < d

-- c) distancia: calcula la distancia euclidea entre dos puntos de R × R
{-
    problema distancia ((a, b) : R × R, (c, d) : R × R): R {
        requiere: { True }
        asegura: { res > 0 }
        asegura: { res = √((c - a)² + (d - b)²) }
    }
-}
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (a, b) (c, d) = sqrt ((c - a) ** 2 + (d - b) ** 2)

-- e) sumarSoloMultiplos: dada una terna de numeros enteros y un natural, calcula la suma de los elementos de la terna que son multiplos del numero natural.
-- sumarSoloMultiplos (10, -8, -5) 2 ⇝ 2
-- sumarSoloMultiplos (66, 21, 4) 5 ⇝ 0
-- sumarSoloMultiplos (-30, 2, 12) 3 ⇝ -18
{-
    problema sumarSoloMultiplos ((a, b, c): Z × Z × Z, n: Z): Z {
        requiere: { n > 0 }
        asegura: { res = multiplo a n + multiplo b n + multiplo c n }
    }
    problema multiplo (x: Z, y: Z): Z {
        requiere: { True }
        asegura: { (mod x y = 0 → res = x) ∨ (mod x y /= 0 → res = 0) }
    }
-}

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a, b, c) n = multiplo a n + multiplo b n + multiplo c n

multiplo :: Integer -> Integer -> Integer
multiplo x y
  | mod x y == 0 = x
  | otherwise = 0

-- f) posPrimerPar: dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno, o devuelve 4 si son todos impares.
{-
    problema posPrimerPar ((a, b, c): Z × Z × Z): Z {
        requiere: { True }
        asegura: { (mod a 2 = 0 → res = 0) ∨ (mod b 2 = 0 → res = 1) ∨ (mod c 2 = 0 → res = 2) ∨ res = 4}
    }
-}
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a, b, c)
  | even a = 0
  | even b = 1
  | even c = 2
  | otherwise = 4

-- g) crearPar :: a -> b -> (a, b): a partir de dos componentes, crea un par con esos valores. Debe funcionar para elementos de cualquier tipo.
{-
    problema crearPar (a: T1, b: T2): T1 × T2{
        requiere: { True }
        asegura: { res = (a, b) }
    }
-}
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

-- h) invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como parametro. Debe funcionar para elementos de cualquier tipo.
{-
    problema crearPar ((a, b): T1 × T2): T2 × T1{
        requiere: { True }
        asegura: { res = (b, a) }
    }
-}
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos: type Punto2D = (Float, Float)
type Punto2D = (Float, Float)

-- productoInterno :: Punto2D -> Punto2D -> Float
-- esParMenor :: Punto2D -> Punto2D -> Bool
-- distancia :: Punto2D -> Punto2D -> Float