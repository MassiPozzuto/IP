{-
Implementar la funcion maximo :: Tablero ->Int
    problema maximo (t: Tablero) : Z {
        requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
        menos un elemento}
        requiere: {Existe al menos una columna en el tablero t }
        requiere: {El tablero t no es vacio, todos los numeros del tablero son positivos, mayor estricto a 0}
        asegura: {res es igual al numero mas grande del tablero t}
    }
-}

type Fila = [Int]

type Tablero = [Fila]

tableroEj :: [[Int]]
tableroEj = [[13, 12, 6, 4], [1, 1, 32, 25], [9, 2, 14, 7], [7, 3, 5, 16], [27, 2, 8, 18]]

maximo :: Tablero -> Int
maximo [fila] = maxFila fila
maximo (primerFila : segundaFila : otrasFilas)
  | maxFila primerFila >= maxFila segundaFila = maximo (primerFila : otrasFilas)
  | otherwise = maximo (segundaFila : otrasFilas)

maxFila :: Fila -> Int
maxFila [el] = el
maxFila (primerEl : segundoEl : otrosEl)
  | primerEl >= segundoEl = maxFila (primerEl : otrosEl)
  | otherwise = maxFila (segundoEl : otrosEl)