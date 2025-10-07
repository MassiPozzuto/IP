{-
Implementar la funcion dineroEnStock :: [(String, Int)] ->[(String, Float)] ->Float
problema dineroEnStock (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : R {
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
    requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
    requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
    requiere: {Todo producto de stock aparece en la lista de precios}
    asegura: {res es igual a la suma de los precios de todos los productos que estan en stock multiplicado por la cantidad de cada producto que hay en stock}
}
Para resolver este ejercicio pueden utilizar la funci´on del Preludio de Haskell fromIntegral que dado un valor de tipo
Int devuelve su equivalente de tipo Float.

-}
stock :: [(String, Int)]
stock = [("Agua", 3), ("Coca", 3), ("Papel Higienico", 2), ("Crema", 4), ("Doritos", 1)]

prices :: [(String, Float)]
prices = [("Agua", 2500.50), ("Coca", 3000.0), ("Papel Higienico", 1500.0), ("Crema", 5000.0), ("Doritos", 1000.0)]

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((prodStock, stock) : otrosProdsStock) prodsPrices = dineroEnStockDeUnSoloProducto + dineroEnStockDeLosOtrosProductos
  where
    dineroEnStockDeUnSoloProducto = dineroEnStockDeUnProducto (prodStock, stock) prodsPrices
    dineroEnStockDeLosOtrosProductos = dineroEnStock otrosProdsStock prodsPrices

dineroEnStockDeUnProducto :: (String, Int) -> [(String, Float)] -> Float
dineroEnStockDeUnProducto _ [] = 0 -- Por especificacion no deberia suceder
dineroEnStockDeUnProducto (prodStock, stock) ((prodPrice, price) : otrosProdsPrices)
  | prodStock == prodPrice = fromIntegral stock * price
  | otherwise = dineroEnStockDeUnProducto (prodStock, stock) otrosProdsPrices