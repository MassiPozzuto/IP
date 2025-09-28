{-
Implementar la funcion masRepetido :: Tablero ->Int
    problema masRepetido (t: Tablero) : Z {
        requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
        menos un elemento}
        requiere: {Existe al menos una columna en el tablero t }
        requiere: {El tablero t no es vacio, todos los numeros del tablero son positivos, mayor estricto a 0}
        asegura: {res es igual al numero que mas veces aparece en un tablero t. Si hay empate devuelve cualquiera de ellos}
    }
-}

type Fila = [Int]

type Tablero = [Fila]

tableroEj :: [[Int]]
tableroEj = [[13, 12, 6, 1], [1, 1, 32, 25], [9, 2, 14, 7], [7, 3, 5, 16], [27, 2, 8, 18]]

masRepetido :: Tablero -> Int
masRepetido tablero = fst (elementoMasRepetido (organizarRepeticionesPorElemento (unificarTablero tablero)))

unificarTablero :: Tablero -> Fila
unificarTablero [] = []
unificarTablero (fila : otrasFilas) = fila ++ unificarTablero otrasFilas

organizarRepeticionesPorElemento :: Fila -> [(Int, Int)]
organizarRepeticionesPorElemento [] = []
organizarRepeticionesPorElemento (primerEl : otrosEl) = (primerEl, cantAparicionesDelPrimerEl) : organizarRepeticionesParaLosDemasEl
  where
    cantAparicionesDelPrimerEl = cantApariciones primerEl (primerEl : otrosEl)
    organizarRepeticionesParaLosDemasEl = organizarRepeticionesPorElemento (quitar primerEl otrosEl)

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar el (x : xs)
  | el == x = quitar el xs
  | otherwise = x : quitar el xs

cantApariciones :: Int -> Fila -> Int
cantApariciones _ [] = 0
cantApariciones el (elFila : otrosElFila)
  | el == elFila = 1 + cantApariciones el otrosElFila
  | otherwise = cantApariciones el otrosElFila

elementoMasRepetido :: [(Int, Int)] -> (Int, Int)
elementoMasRepetido [x] = x
elementoMasRepetido ((primerEl, cantPrimerEl) : (segundoEl, cantSegundoEl) : otrosEl)
  | cantPrimerEl >= cantSegundoEl = elementoMasRepetido ((primerEl, cantPrimerEl) : otrosEl)
  | otherwise = elementoMasRepetido ((segundoEl, cantSegundoEl) : otrosEl)