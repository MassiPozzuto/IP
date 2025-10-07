{-
Implementar la funcion divisoresPropios :: Int ->[Int]
    problema divisoresPropios (n: Z) : seq⟨Z⟩ {
        requiere: {n > 0}
        asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
        asegura: {res no tiene elementos repetidos}
        asegura: {res no contiene a ningun elemento que no sea un divisor propio de n}
    }
-}

divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresPropiosAux n 1

divisoresPropiosAux :: Int -> Int -> [Int]
divisoresPropiosAux n i
  | n == i = [] -- El numero mismo no se tiene en cuenta en los divisores propios (y tiene logica)
  | mod n i == 0 = i : divisoresPropiosAux n (i + 1)
  | otherwise = divisoresPropiosAux n (i + 1)