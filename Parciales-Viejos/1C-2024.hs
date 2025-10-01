{--
La Unidad de Tecnologías de la Información (UTI) de nuestra Facultad nos ha encargado que desarrollemos un nuevo sistema para el registro de alumnos. En este sistema 
se guarda la información de cada alumno, que está representada como una tupla de dos elementos: el primero es el nombre completo del alumno y el segundo una lista 
con las notas de los finales que rindió.

Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos 
y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).

Ejercicio 1 (2 puntos) 
    problema aproboMasDeNMaterias (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, alumno:seq⟨Char⟩, n: Z) : Bool {
        requiere: {No hay nombres de alumnos repetidos en registro}
        requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
        requiere: {n > 0}
        requiere: {El alumno se encuentra en el registro }
        asegura: {res = true <=> el alumno tiene más de n notas de finales mayores o iguales a 4 en el registro}
    }

--}
aproboMasDeNMaterias :: [(String, [Integer])] -> String -> Integer -> Bool
aproboMasDeNMaterias [] _ _ = False
aproboMasDeNMaterias ((alumno, notas): otrosAlumnos) alumnoDeseado cantMaterias
    | alumno == alumnoDeseado = cantNotasAprobadas notas > cantMaterias
    | otherwise = aproboMasDeNMaterias otrosAlumnos alumnoDeseado cantMaterias

cantNotasAprobadas :: [Integer] -> Integer
cantNotasAprobadas [] = 0
cantNotasAprobadas (nota: otrosNotas)
    | nota >= 4 = 1 + cantNotasAprobadas otrosNotas
    | otherwise = cantNotasAprobadas otrosNotas

{--

Ejercicio 2 (2 puntos)
    problema buenosAlumnos (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨seq⟨Char⟩⟩ {
        requiere: {No hay nombres de alumnos repetidos en registro}
        requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
        asegura: {res es la lista de los nombres de los alumnos que están en registro cuyo promedio de notas es mayor o igual a 8 y no tiene aplazos (notas menores que 4)}
    }
Para resolver el promedio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve su equivalente de tipo Float.

--}
buenosAlumnos :: [(String, [Integer])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((alumno, notas): otrosAlumnos)
    | (promedio notas >= 8) && (cantAplazos notas == 0) = alumno : buenosAlumnos otrosAlumnos
    | otherwise = buenosAlumnos otrosAlumnos

promedio :: [Integer] -> Float
promedio lst = fromIntegral (sumatoria lst) / fromIntegral (longitud lst)

sumatoria :: (Num t) => [t] -> t
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

longitud :: [t] -> Integer
longitud [] = 0
longitud (el: otrosEl) = 1 + longitud otrosEl

cantAplazos :: [Integer] -> Integer
cantAplazos [] = 0
cantAplazos (nota: otrasNotas)
    | nota < 4 = 1 + cantAplazos otrasNotas
    | otherwise = cantAplazos otrasNotas

{--

Ejercicio 3 (2 puntos)
    problema mejorPromedio (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨Char⟩ {
        requiere: {No hay nombres de alumnos repetidos en registro}
        requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
        requiere: {|registro| > 0 }
        asegura: {res es el nombre del alumno cuyo promedio de notas es el más alto; si hay más de un alumno con el mismo promedio de notas, devuelve el nombre de alumno que aparece primero en registro}
    }

--}
mejorPromedio :: [(String, [Integer])] -> String
mejorPromedio [(alumno, notas)] = alumno
mejorPromedio ((alumno, notas): otrosAlumnos)
    | promedio notas >= mejorPromedioNum otrosAlumnos = alumno
    | otherwise = mejorPromedio otrosAlumnos        

mejorPromedioNum :: [(String, [Integer])] -> Float
mejorPromedioNum [(alumno, notas)] = promedio notas
mejorPromedioNum ((alumno, notas): otrosAlumnos)
    | promedio notas >= mejorPromedioNum otrosAlumnos = promedio notas
    | otherwise = mejorPromedioNum otrosAlumnos

{--

Ejercicio 4 (3 puntos)
    problema seGraduoConHonores (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, cantidadDeMateriasDeLaCarrera: Z, alumno: seq⟨Char⟩ ) : Bool {
        requiere: {No hay nombres de alumnos repetidos en registro}
        requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
        requiere: {cantidadDeMateriasDeLaCarrera > 0}
        requiere: {El alumno se encuentra en el registro }
        requiere: {|buenosAlumnos(registro)| > 0}
        asegura: {res <=> true si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera -1) = true y alumno pertenece al conjunto de buenosAlumnos(registro) y el promedio de notas de finales de alumno está a menos (estrictamente) de 1 punto del mejorPromedio(registro)}
    }

--}

registroEj :: [(String, [Integer])]
registroEj = [("Pedro", [10, 8, 6, 3, 10, 10, 9]), ("Juan", [9, 9, 8]), ("Simon", [10,8,6,10,6])]

seGraduoConHonores :: [(String, [Integer])] -> Integer -> String -> Bool
seGraduoConHonores ((alumno, notas): otrosAlumnos) cantMateriasCarrera alumnoDeseado
    | alumno == alumnoDeseado = alumnoAproboMasDeNMaterias && alumnoEsBuenAlumno && (promedio notas > mejorPromedioNum registro - 1)
    | otherwise = seGraduoConHonores otrosAlumnos cantMateriasCarrera alumnoDeseado
    where 
        alumnoAproboMasDeNMaterias = aproboMasDeNMaterias registro alumno (cantMateriasCarrera -1)
        alumnoEsBuenAlumno = pertenece (buenosAlumnos registro) alumno
        registro = (alumno, notas): otrosAlumnos

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece [] _ = False
pertenece (x:xs) el
    | el == x = True
    | otherwise = pertenece xs el

{--

Ejercicio 5 (1 punto)
Conteste marcando la opción correcta. El Testing es una técnica de verificación que sirve para:
○ Demostrar que un programa es correcto.
○ Probar propiedades de un programa.
● Encontrar fallas en un programa.

--}