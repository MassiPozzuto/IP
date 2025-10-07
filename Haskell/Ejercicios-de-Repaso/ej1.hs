{-

Implementar la funcion generarStock :: [String] ->[(String, Int)]
    problema generarStock (mercaderia: seq⟨String⟩) : seq⟨String × Z⟩ {
        requiere: {True}
        asegura: { La longitud de res es igual a la cantidad de productos distintos que hay en mercaderia}
        asegura: {Para cada producto que pertenece a mercaderia, existe un i tal que 0 ≤ i < |res| y res[i]0=producto y res[i]1 es igual a la cantidad de veces que aparece producto en mercaderia}
    }

-}

mercaderia = ["Agua", "Coca", "Papel Higienico", "Crema", "Agua", "Doritos", "Coca", "Coca", "Crema", "Agua", "Papel Higienico", "Crema", "Crema"]

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (producto : otrosProductos) = (producto, cantDeAparicionesDelProd) : generarStock demasProductos
  where
    cantDeAparicionesDelProd = 1 + contarProducto producto otrosProductos -- El +1 es porque faltaria contar producto
    demasProductos = quitar producto otrosProductos

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar el (x : xs)
  | el == x = quitar el xs
  | otherwise = x : quitar el xs

contarProducto :: String -> [String] -> Int
contarProducto _ [] = 0
contarProducto prod (primerProd : otrosProds)
  | prod == primerProd = 1 + contarProducto prod otrosProds
  | otherwise = contarProducto prod otrosProds