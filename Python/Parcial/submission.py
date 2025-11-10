from queue import Queue as Cola

# Ejercicio 1
def cantidad_subsecuencias_que_suman(s: list[int], n: int) -> int:
	res: int = 0
	
	subsecuencias_consecutivas: list[list[int]] = obtener_subsecuencias_consecutivas(s)
	for subsecuencia in subsecuencias_consecutivas:
		sumatoria_subsecuencia_actual:int = 0
		for num in subsecuencia:
			sumatoria_subsecuencia_actual += num
		
		if sumatoria_subsecuencia_actual == n:
			res += 1
		
	return res

def obtener_subsecuencias_consecutivas(lista: list[int]) -> list[list[int]]:
	res: list[list[int]] = []

	for i in range(len(lista)):
		subsecuencia_actual: list[int] = []
		for j in range(i, len(lista)):
			subsecuencia_actual.append(lista[j])
			res.append(subsecuencia_actual.copy())

	return res


# Ejercicio 2
def abrir_caja_prioridad(clientes: Cola[tuple[str, bool]]) -> Cola[str]:
	res: Cola[str] = Cola()
	cola_aux: Cola[tuple[str, bool]] = Cola()
	
	while not clientes.empty():
		cliente_actual: tuple[str, bool] = clientes.get()
		if cliente_actual[1]:
			res.put(cliente_actual[0])
		else:
			cola_aux.put(cliente_actual)

	while not cola_aux.empty():
		clientes.put(cola_aux.get())
	
	return res


# Ejercicio 3
def buscar_columna_con_maximo_menor_a_cota(A: list[list[int]], cota: int) -> int:
	col_maximo_menor_a_cota:int = 0
	maximo_menor_a_cota:int = A[0][0]
	for fila in A:
		for j in range(len(fila)):
			# maximo_menor_a_cota >= cota: solamente es porque su valor default es A[0][0] y podria exceder o igualar al valor de la cota
			if (fila[j] < cota and fila[j] > maximo_menor_a_cota) or maximo_menor_a_cota >= cota: 
				maximo_menor_a_cota = fila[j]
				col_maximo_menor_a_cota = j

	return col_maximo_menor_a_cota


# Ejercicio 4
def agrupar_por_autor_con_cota(libros: dict[str, str], cota: int) -> dict[str, list[str]]:
	res: dict[str, list[str]] = {}
	for libro, autor in libros.items():
		if cantidad_apariciones_autor(libros, autor) >= cota:
			if autor not in res.keys():
				res[autor] = [libro]
			else:
				res[autor].append(libro)
			
	return res

def cantidad_apariciones_autor(libros: dict[str, str], autor_buscado: str) -> int:
	res: int = 0
	for autor in libros.values():
		if autor == autor_buscado:
			res += 1

	return res