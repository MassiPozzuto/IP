{-
Implementar la funcion iesimoDigito :: Integer ->Integer ->Integer que dado un n ∈ Z mayor o igual a 0 y un i ∈ Z mayor o igual a 1 y menor o igual a la cantidad de digitos de n, devuelve el i-esimo digito de n.

    problema iesimoDigito (n: Z, i: Z) : Z {
        requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
        asegura: { resultado = (n div 10^(cantDigitos(n)−i)) mod 10 }
    }

    problema cantDigitos (n: Z) : N {
        requiere: { n ≥ 0 }
        asegura: { n = 0 → resultado = 1}
        asegura: { n ̸= 0 → ((n div 10^(resultado−1) > 0) ∧ (n div 10^(resultado) = 0)) }
    }
-}

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n 1 = mod n 10
iesimoDigito n i = iesimoDigito (div n 10) (i - 1)
