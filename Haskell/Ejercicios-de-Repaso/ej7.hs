{-
Implementar la funcion valoresDeCamino :: Tablero ->Camino ->[Int]
    problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
        requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al menos un elemento}
        requiere: {Existe al menos una columna en el tablero t }
        requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
        requiere: {El camino c es un camino v´alido, es decir, secuencia de posiciones adyacentes en la que solo es posible desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero t}
        asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen las posiciones correspondientes en el camino.}
    }
-}

type Fila = [Int]

type Tablero = [Fila]

type Posicion = (Int, Int)

type Camino = [Posicion]

tableroEj :: [[Int]]
tableroEj = [[13, 12, 6, 4], [1, 1, 32, 25], [9, 2, 14, 7], [7, 3, 5, 16], [27, 2, 8, 18]]

caminoEj :: [(Int, Int)]
caminoEj = [(2, 1), (2, 2), (3, 2), (4, 2), (4, 3)]

--

valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino tablero ((i, j) : otrasPosiciones) = buscarCoordenada tablero (i - 1, j - 1) : valoresDeCamino tablero otrasPosiciones

-- Restamos 1 a i y a j ya que las posiciones empiezan desde 1 y en las listas de Haskell empiezan desde 0

buscarCoordenada :: Tablero -> Posicion -> Int
buscarCoordenada (fila : otrasFilas) (i, j)
  | i == 0 = buscarPosicionEnUnaFila fila j
  | otherwise = buscarCoordenada otrasFilas (i - 1, j)

buscarPosicionEnUnaFila :: Fila -> Int -> Int
buscarPosicionEnUnaFila (el : otrosEl) j
  | j == 0 = el
  | otherwise = buscarPosicionEnUnaFila otrosEl (j - 1)