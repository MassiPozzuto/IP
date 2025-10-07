{-
Implementar la funcion aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
    problema aplicarOferta (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : seq⟨String × R⟩ {
        requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
        requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
        requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
        requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
        requiere: {Todo producto de stock aparece en la lista de precios}
        asegura: {|res| = |precios|}
        asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) > 10, entonces res[i]0 = precios[i]0 y
        res[i]1 = precios[i]1∗ 0,80}
        asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) ≤ 10, entonces res[i]0 = precios[i]0 y
        res[i]1 = precios[i]1 }
    }
-}
stock :: [(String, Int)]
stock = [("Agua", 13), ("Coca", 3), ("Papel Higienico", 2), ("Crema", 32), ("Doritos", 11)]

prices :: [(String, Float)]
prices = [("Agua", 2500.0), ("Coca", 3000.0), ("Papel Higienico", 1500.0), ("Crema", 5000.0), ("Doritos", 1000.0)]

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta _ [] = []
aplicarOferta stock ((prodPrice, price) : otrosProdsPrices)
  | stockDeProducto stock prodPrice > 10 = (prodPrice, price * 0.80) : aplicarOferta stock otrosProdsPrices
  | otherwise = (prodPrice, price) : aplicarOferta stock otrosProdsPrices

-- Lo hice en el ej2.hs
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((prod, stock) : otrosProds) prodDeseado
  | prodDeseado == prod = stock
  | otherwise = stockDeProducto otrosProds prodDeseado