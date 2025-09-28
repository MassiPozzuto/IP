{-
Implementar la funcion sonAmigos :: Int ->Int ->Bool
    problema sonAmigos (n,m: Z) : Bool {
        requiere: {n > 0}
        requiere: {m > 0}
        requiere: {m ̸= n}
        asegura: {res = True ⇔ n y m son numeros amigos}
    }
-}

sonAmigos :: Int -> Int -> Bool
sonAmigos n m = (sumatoriaDeElementos (divisoresPropios n) == m) && (sumatoriaDeElementos (divisoresPropios m) == n)

-------- Funciones del ejercicio anterior -----------
divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresPropiosAux n 1

divisoresPropiosAux :: Int -> Int -> [Int]
divisoresPropiosAux n i
  | n == i = [] -- El numero mismo no se tiene en cuenta en los divisores propios (y tiene logica)
  | mod n i == 0 = i : divisoresPropiosAux n (i + 1)
  | otherwise = divisoresPropiosAux n (i + 1)

---------------------------------------------------

sumatoriaDeElementos :: (Num t) => [t] -> t
sumatoriaDeElementos [] = 0
sumatoriaDeElementos (x : xs) = x + sumatoriaDeElementos xs
