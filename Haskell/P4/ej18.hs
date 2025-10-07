{-

Implementar una funcion mayorDigitoPar :: Integer ->Integer segun la siguiente especificacion:

    problema mayorDigitoPar (n: N) : N {
        requiere: { True }
        asegura: { resultado es el mayor de los digitos pares de n. Si n no tiene ningun digito par, entonces resultado es -1.}
    }

-}

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n
  | n < 10 && (mod n 2 /= 0) = -1
  | (mod (ultimoDigito n) 2 == 0) && (ultimoDigito n >= mayorDigitoPar (div n 10)) = ultimoDigito n
  | otherwise = mayorDigitoPar (div n 10)

ultimoDigito :: Integer -> Integer
ultimoDigito n
  | n < 10 = n
  | otherwise = mod n 10