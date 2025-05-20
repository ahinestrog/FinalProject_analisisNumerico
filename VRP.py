from Vehiculo import *
from Nodo import *
import math

def main ():
    vehiculos = []
    for i in range(20):
        vehiculo = Vehiculo(i+1)
        vehiculos.append(vehiculo)
    
    nodos = []
    with open("Coord.txt", "r") as f:
        with open("Dist.txt", "r") as f2:
            for i in range(200):
                line = f.readline()
                line2 = f2.readline()
                line2 = list(map(float, line2.split()))
                x, y = map(float, line.split())
                nodo = Nodo(i+1, x, y, line2)
                print(nodo.id, nodo.x, nodo.y, nodo.distancia)
                nodos.append(nodo)
        


if __name__ == "__main__":
    main()
