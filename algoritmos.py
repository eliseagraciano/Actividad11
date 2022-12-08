from math import sqrt
def distancia_euclidiana(x_1, y_1, x_2, y_2):
    """ Calcula la distancia euclidiana
	
	Devuelve el resultado de la fórmula 

	También se le conoce a la fórmula como:
	distancia entre dos puntos

	Parámetros:
	x_1 -- origen_x
	y_1 -- origen_y
	x_2 -- destino_x
	y_2 -- destino_y

	"""
    return(sqrt(((x_2 - x_1)**2) + ((y_2 - y_1)**2)))


