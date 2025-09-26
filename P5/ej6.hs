-- En este ejercicio trabajaremos con la lista de contactos del telefono.
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]
-- Sugerencia: Implementar las funciones auxiliares elNombre y elTelefono para que dado un Contacto devuelva el dato del nombre y el telefono respectivamente.

listaDeContactos = [("Fede", "123"), ("Valen", "456"), ("Massi", "789")]

-- a) Implementar una funcion que me diga si una persona aparece en mi lista de contactos del telefono: enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((nomPrimerContacto, _): otrosContactos) = nombre == nomPrimerContacto || estaEnLosOtrosContactos
    where 
        estaEnLosOtrosContactos = enLosContactos nombre otrosContactos

--b) Implementar una funcion que agregue una nueva persona a mis contactos, si esa persona esta ya en mis contactos entonces actualiza el telefono. agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (nomNuevo, telNuevo) [] = [(nomNuevo, telNuevo)]
agregarContacto (nomNuevo, telNuevo) ((nomPrimerContacto, telPrimerContacto): otrosContactos)
    | nomNuevo == nomPrimerContacto = nuevoContacto : otrosContactos
    | otherwise = primerContacto : (agregarContacto nuevoContacto otrosContactos)
    where 
        primerContacto = (nomPrimerContacto, telPrimerContacto) 
        nuevoContacto = (nomNuevo, telNuevo)

-- c) Implementar una funcion que dado un nombre, elimine un contacto de mis contactos. Si esa persona no esta no hace nada. eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre ((nomPrimerContacto, telPrimerContacto): otrosContactos) 
    | nombre == nomPrimerContacto = otrosContactos
    | otherwise = (nomPrimerContacto, telPrimerContacto): eliminarDeLosOtrosContactos
    where 
        eliminarDeLosOtrosContactos = eliminarContacto nombre otrosContactos
