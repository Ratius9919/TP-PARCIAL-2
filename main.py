def crear_matriz(n, m):
    return [[0] * m for fila in range(n)]


def llenar_matriz(m):
    filas = len(m)
    columnas = len(m[0])
    for f in range(filas):
        for c in range(columnas):
            m[f][c] = lista = []


def mostrar_matriz(m):
    a = 1
    for fila in m:
        print("Mes", a, fila, ":")
        a += 1


def ajustar_meses(m):
    filas = len(m)
    columnas = len(m[0])
    a = 0
    for f in range(filas):

        if f == 1:
            febrero = m[f][1:29]
            m[f] = febrero
        elif f == 3 or f == 5 or f == 8 or f == 10:
            mes = m[f][1:30]
            m[f] = mes


meses = 12
dias = 31
turnos_meses_dias = crear_matriz(12, dias)
llenar_matriz(turnos_meses_dias)

ajustar_meses(turnos_meses_dias)

mostrar_matriz(turnos_meses_dias)
