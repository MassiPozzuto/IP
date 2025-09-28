{-
Implementar la funcion listaDeAmigos :: [Int] ->[(Int,Int)]
    problema listaDeAmigos (lista: seq⟨Z⟩) : seq⟨Z × Z⟩ {
        requiere: {Todos los numeros de lista son mayores a 0}
        requiere: {Todos los numeros de lista son distintos}
        asegura: {res es una lista de tuplas sin repetidos, que contiene a todos los pares de numeros que pertenecen a lista y son amigos entre si}
        asegura: {|res| es igual a la cantidad de pares de n´umeros amigos que hay en lista.}
    }

Ejemplos de pares de numeros amigos: (220,284), (1184,1210)
-}

listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [] = []
listaDeAmigos (x : xs)
  | encontrarAmigo x xs == 0 = listaDeAmigos xs
  | otherwise = (x, encontrarAmigo x xs) : listaDeAmigos xs

encontrarAmigo :: Int -> [Int] -> Int
encontrarAmigo _ [] = 0
encontrarAmigo n (x : xs)
  | sonAmigos n x = x
  | otherwise = encontrarAmigo n xs

-------- Funciones de los ejercicios anteriores --------------
sonAmigos :: Int -> Int -> Bool
sonAmigos n m = (sumatoriaDeElementos (divisoresPropios n) == m) && (sumatoriaDeElementos (divisoresPropios m) == n)

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