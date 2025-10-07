{-
Implementar la funcion losPrimerosNPerfectos :: Int ->[Int]
    problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
        requiere: {n > 0}
        asegura: {|res| = n}
        asegura: {res es la lista de los primeros n numeros perfectos, de menor a mayor}
    }
Por cuestiones de tiempos de ejecucion, no les recomendamos que prueben este ejercicio con un n > 4.
-}

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = losPrimerosNPerfectosAux n 1 []

--- Se que la funcion length no se puede usar en el parcial, pero es una funcion muy pelotuda para hacerla a parte
losPrimerosNPerfectosAux :: Int -> Int -> [Int] -> [Int]
losPrimerosNPerfectosAux n i actualesNumPerfectos
  | length actualesNumPerfectos == n = actualesNumPerfectos
  | sumatoriaDeElementos (divisoresPropios i) == i = losPrimerosNPerfectosAux n (i + 1) (actualesNumPerfectos ++ [i])
  | otherwise = losPrimerosNPerfectosAux n (i + 1) actualesNumPerfectos

-------- Funciones de los ejercicios anteriores --------------
divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresPropiosAux n 1

divisoresPropiosAux :: Int -> Int -> [Int]
divisoresPropiosAux n i
  | n == i = [] -- El numero mismo no se tiene en cuenta en los divisores propios (y tiene logica)
  | mod n i == 0 = i : divisoresPropiosAux n (i + 1)
  | otherwise = divisoresPropiosAux n (i + 1)

sumatoriaDeElementos :: (Num t) => [t] -> t
sumatoriaDeElementos [] = 0
sumatoriaDeElementos (x : xs) = x + sumatoriaDeElementos xs

--------------------------------------------------------------