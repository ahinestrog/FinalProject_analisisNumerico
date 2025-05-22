from Vehiculo import *
from Nodo import *
import math
import numpy as np
import matplotlib.pyplot as plt
import time

# Leer los archivos .txt (Dist.txt y Coord.txt)
dist_matrix = np.loadtxt("Dist.txt")        
coords = np.loadtxt("Coord.txt")

# Crear los nodos con distancia inicial 0 (Deposito en 0.0)
nodos = []
for i in range(len(coords)):
    nodo = Nodo(i, coords[i][0], coords[i][1], 0.0)
    nodos.append(nodo)

def construir_rutas():
    clientes = []
    for i in range(1, 200):
        clientes.append(i)

    vehiculos = []
    vehiculoId = 0

    while len(clientes) > 0:
        v = Vehiculo(vehiculoId)
        vehiculoId += 1
        actual = 0
        capacidad = 12
        distancia_total = 0.0

        v.ruta.append(0)  

        while capacidad > 0 and len(clientes) > 0:
            menor_distancia = float("inf")
            siguiente = -1

            for c in clientes:
                d = dist_matrix[actual][c]
                if d < menor_distancia:
                    menor_distancia = d
                    siguiente = c

            if siguiente != -1:
                v.ruta.append(siguiente)
                distancia_total += menor_distancia
                clientes.remove(siguiente)
                actual = siguiente
                capacidad -= 1

        v.ruta.append(0)
        distancia_total += dist_matrix[actual][0]

        for i in range(1, len(v.ruta)):
            desde = v.ruta[i - 1]
            hasta = v.ruta[i]
            nodos[hasta].distancia = dist_matrix[desde][hasta]

        vehiculos.append(v)

    return vehiculos

# Gráficos de las rutas
def graficar_rutas(vehiculos):
    plt.figure(figsize=(10, 8))

    for v in vehiculos:
        x = []
        y = []
        for i in v.ruta:
            x.append(nodos[i].x)
            y.append(nodos[i].y)
        plt.plot(x, y, marker='o')

    plt.scatter(nodos[0].x, nodos[0].y, c='red', s=100, label='Depósito')
    plt.title("Rutas de vehículos")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    inicio = time.time()

    vehiculos = construir_rutas()

    distancia_total = 0.0
    for v in vehiculos:
        suma = 0.0
        for i in range(1, len(v.ruta)):
            desde = v.ruta[i - 1]
            hasta = v.ruta[i]
            d = dist_matrix[desde][hasta]
            suma += d
        print("Vehículo", v.vehiculoId, "- Clientes atendidos:", len(v.ruta) - 2, "- Distancia:", round(suma, 2))
        distancia_total += suma

    print("\nTotal de vehículos usados:", len(vehiculos))
    print("Distancia total recorrida:", round(distancia_total, 2))
    print("Tiempo de ejecución:", round(time.time() - inicio, 2), "segundos")

    graficar_rutas(vehiculos)

if __name__ == "__main__":
    main()
