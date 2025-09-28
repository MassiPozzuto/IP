{-
Implementar la funcion stockDeProducto :: [(String, Int)] ->String ->Int
    problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String ) : Z {
        requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
        requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
        asegura: {si no existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a 0 }
        asegura: {si existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a stock[i]1 }
    }

-}

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((prod, stock) : otrosProds) prodDeseado
  | prodDeseado == prod = stock
  | otherwise = stockDeProducto otrosProds prodDeseado