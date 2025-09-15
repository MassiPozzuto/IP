{-
Implementar una funcion estanRelacionados :: Integer -> Integer -> Bool
    problema estanRelacionados (a : Z, b : Z) : Bool {
        requiere: {a ̸= 0 ∧ b ̸= 0}
        asegura: {(res = true) ↔ (a ∗ a + a ∗ b ∗ k = 0 para algun k ∈ Z con k ̸= 0)}
    }

Por ejemplo:
estanRelacionados 8 2 ⇝ True porque existe k = −4 tal que 8 × 8 + 8 × 2 × (−4) = 0
estanRelacionados 7 3 ⇝ False porque no existe un k entero tal que 7 × 7 + 7 × 3 × k = 0
-}

{-
Reemplazando la ecuacion queda:
    k = -(a/b)
Si k tiene que ser entero, entonces la division entre a y b debe dar como resto 0.
Viendolo desde otro punto solo si a es multiplo de b, la ecuacion se cumple
-}
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = mod a b == 0