
laberinto = [
    ['F',1,1,3,0,1,1,1,4],
    [3,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,3,1,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,3,1,1,1,1],
    [1,0,0,1,0,1,0,0,4],
    ['I',1,3,1,0,1,1,1,1]

]
n = 9
puntos_minimos = 23
direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
path = [[0 for _ in range(n)] for _ in range(n)]
visitado = [[False for _ in range(n)] for _ in range(n)]
encontrado = False
puntos_totales = 0  

def puntos(x, y):
    return laberinto[x][y] if laberinto[x][y] in [3, 4] else 0

def es_valido(x, y, visitado):
    return 0 <= x < n and 0 <= y < n and not visitado[x][y] and laberinto[x][y] != 0

def backtrack(x, y, puntos_actuales, visitado):
    global encontrado, puntos_totales

    if (x, y) == (0, 0):
        if puntos_actuales >= puntos_minimos:
            path[x][y] = 1
            puntos_totales = puntos_actuales 
            encontrado = True
            return True
        return False

    visitado[x][y] = True
    path[x][y] = 1

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            nueva_suma = puntos_actuales + puntos(nx, ny)
            if backtrack(nx, ny, nueva_suma, visitado):
                return True

    path[x][y] = 0
    visitado[x][y] = False
    return False

inicio_x, inicio_y = 8, 0
backtrack(inicio_x, inicio_y, puntos(inicio_x, inicio_y), visitado)

print("Laberinto original:")
for fila in laberinto:
    print(fila)

print("\nResultado:")
if encontrado:
    print(f"Se encontro un camino valido con {puntos_totales} puntos")
    if puntos_totales == 23:
        print("El ratón llegó con exactamente 23 puntos")
    else:
        print("No se encontró un camino valido con al menos 23 puntos")

print("\nCamino recorrido por el raton (1 = paso, 0 = no paso):")
for fila in path:
    print(fila)