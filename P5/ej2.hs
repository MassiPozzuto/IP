-- Definir las siguientes funciones sobre listas:

-- 1. pertenece :: (Eq t) => t -> [t] -> Bool segun la siguiente especificacion:
{-
    problema pertenece (e: T, s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { resultado = true ↔ e ∈ s }
    }
-}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x : xs) = (e == x) || pertenece e xs

-- 2. todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero si y solamente si todos sus elementos son iguales.
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x : y : xs) = (x == y) && todosIguales (x : xs)

-- 3. todosDistintos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
{-
    problema todosDistintos (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
    }
-}
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x : y : xs) = (x /= y) && todosDistintos (x : xs) && todosDistintos (y : xs)

-- 4. hayRepetidos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
{-
    problema hayRepetidos (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
    }
-}
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos t = not (todosDistintos t)

-- 5. quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparicion de x en la lista xs (de haberla).
quitar :: (Eq t) => t -> [t] -> [t]
quitar k [] = []
quitar k (x : xs)
  | k == x = xs
  | otherwise = x : quitar k xs

-- 6. quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones de x en la lista xs (de haberlas). Es decir:
{-
    problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { True }
        asegura: { resultado es igual a s pero sin el elemento e. }
    }
-}
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos k [] = []
quitarTodos k (x : xs)
  | k == x = quitarTodos k xs
  | otherwise = x : quitarTodos k xs

-- 7. eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una unica aparicion de cada elemento, eliminando las repeticiones adicionales.
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x : xs)
  | cantDeApariciones x xs > 0 = x : eliminarRepetidos (quitarTodos x xs)
  | otherwise = x : eliminarRepetidos xs

cantDeApariciones :: (Eq t) => t -> [t] -> Integer
cantDeApariciones el [] = 0
cantDeApariciones el (x : xs)
  | el == x = 1 + cantDeApariciones el xs
  | otherwise = cantDeApariciones el xs

-- Otra forma
eliminarRepetidos' :: (Eq t) => [t] -> [t]
eliminarRepetidos' [] = []
eliminarRepetidos' (x : xs) = x : eliminarRepetidos' (quitarTodos x xs)

-- 8. mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero si y solamente si ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
{-
    problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
    }
-}
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos x y = tieneTodosLosElementosDeXLista x y && tieneTodosLosElementosDeXLista y x

tieneTodosLosElementosDeXLista :: (Eq t) => [t] -> [t] -> Bool
tieneTodosLosElementosDeXLista [] _ = True
tieneTodosLosElementosDeXLista _ [] = True
tieneTodosLosElementosDeXLista (el : otrosEl) lista
  | not (pertenece el lista) = False
  | otherwise = tieneTodosLosElementosDeXLista otrosEl lista

-- 9. capicua :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
{-
    problema capicua (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { (resultado = true) ↔ (s = reverso(s)) }
    }

Por ejemplo:
    capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true,
    capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false.
-}

capicua :: (Eq t) => [t] -> Bool
capicua t = t == reverso t

reverso :: [t] -> [t]
reverso [] = []
reverso t = ultimo t : reverso (principio t)

principio :: [t] -> [t]
principio [x] = []
principio (x : xs) = x : principio xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs