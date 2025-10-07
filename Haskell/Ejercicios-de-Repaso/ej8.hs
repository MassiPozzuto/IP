{-
Implementar la funcion esCaminoFibo :: [Int] ->Int ->Bool
    problema esCaminoFibo (s:seq⟨Z⟩, i : Z) : Bool {
        requiere: {La secuencia de numeros s es no vacia y esta compuesta por numeros positivos (mayores estrictos a 0) que representan los numeros ubicados en las posiciones que forman un camino en un tablero}
        requiere: {i ≥ 0}
        asegura: {res = true ⇔ los valores de s son la sucesi´on de Fibonacci inicializada con el numero pasado como parametro i}
    }

En el ejemplo del tablero y del camino (verde claro) que figuran mas arriba tenemos que esCaminoFibo [1,1,2,3,5] 1 reduce a True.
esCaminoFibo (valoresDeCamino tablero [(3,2), (4, 2), (4,3)]) 3, siendo tablero el del ejemplo, tambien reduce aTrue.
-}

esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] _ = True
esCaminoFibo (el : otrosEl) i
  | el == fibonacci i = esCaminoFibo otrosEl (i + 1)
  | otherwise = False

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)