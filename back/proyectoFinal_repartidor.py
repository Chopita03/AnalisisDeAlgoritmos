import math
import matplotlib.pyplot as plt

def organizar_paquetes(camiones, paquetes):
    # Ordenar los paquetes por espacio de menor a mayor
    paquetes_ordenados = sorted(paquetes.items(), key=lambda x: x[1]["espacio"])

    # Inicializar lista de resultado
    resultado = []

    for camion, capacidad in camiones.items():
        espacio_disponible = capacidad
        paquetes_en_camion = {}

        for paquete, info_paquete in paquetes_ordenados:
            if info_paquete["espacio"] <= espacio_disponible and paquete not in paquetes_en_camion:
                paquetes_en_camion[paquete] = info_paquete["coordenadas"]
                espacio_disponible -= info_paquete["espacio"]

        resultado.append({camion: paquetes_en_camion})

        # Actualizar la lista de paquetes disponibles
        paquetes_ordenados = [(p, info) for p, info in paquetes_ordenados if p not in paquetes_en_camion]

    return resultado

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad2[0] - ciudad1[0])**2 + (ciudad2[1] - ciudad1[1])**2)

def viajero_comercio(almacen, clientes):
    destinos = [almacen] + list(clientes.values())
    num_destinos = len(destinos)
    visitados = [False] * num_destinos
    ruta = [0]  # Comienza en el almacén
    visitados[0] = True

    for _ in range(num_destinos - 1):
        ciudad_actual = ruta[-1]
        distancia_minima = float('inf')
        siguiente_ciudad = None

        for i in range(num_destinos):
            if not visitados[i]:
                dist = distancia(destinos[ciudad_actual], destinos[i])
                if dist < distancia_minima:
                    distancia_minima = dist
                    siguiente_ciudad = i

        ruta.append(siguiente_ciudad)
        visitados[siguiente_ciudad] = True

    ruta.append(0)  # Regresa al almacén al final

    distancia_total = sum(distancia(destinos[ruta[i]], destinos[ruta[i + 1]]) for i in range(num_destinos))

    return ruta, distancia_total

def dibujar_ruta(camino, destinos, mejor_distancia):
    x = [destinos[i][0] for i in camino]
    y = [destinos[i][1] for i in camino]
    x.append(x[0])
    y.append(y[0])
    
    plt.figure()
    plt.plot(x, y, 'x-')
    plt.scatter(x[1:-1], y[1:-1], c='red', marker='o')  # Marcadores para clientes
    
    # Etiquetas para el almacén y clientes
    plt.text(x[0], y[0], 'Almacén', ha='right', va='bottom', fontweight='bold')
    for i, cliente in enumerate(destinos[1:]):
        plt.text(cliente[0], cliente[1], f'C{i+1}', ha='right', va='bottom', fontweight='bold')
    
    plt.title(f"Ruta óptima con distancia {mejor_distancia:.2f}")
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()

def main():

    # Ejemplo de datos de entrada para la funcion de organizar paquetes
    camiones = {"camion1": 10, "camion2": 15}

    paquetes = {
        "P1": {"espacio": 2, "coordenadas": (42.360613, -71.058556)},
        "P2": {"espacio": 7, "coordenadas": (42.361163, -71.057242)},
        "P3": {"espacio": 3, "coordenadas": (42.360200, -71.056934)},
        "P4": {"espacio": 5, "coordenadas": (42.359270, -71.057078)},
        "P5": {"espacio": 8, "coordenadas": (42.360350, -71.059055)}
    }

    # Ejemplo de datos de entrada para el programa de las rutas
    almacen = (42.359998, -71.058502)

    # Esto esta comentado porque en vez de usar estos usara los que genera la funcion de organizar los paquetes
    """
    clientes = {
        'C1': (42.360613, -71.058556),
        'C2': (42.361163, -71.057242),
        'C3': (42.360200, -71.056934),
        'C4': (42.359270, -71.057078),
        'C5': (42.360350, -71.059055),
        'C6': (42.361056, -71.059242),
        'C7': (42.361670, -71.058636)
    }
    """

    # Obtener la lista con los diccionarios de cada camion
    orden_camiones = organizar_paquetes(camiones, paquetes)

    # Imprimir la lista de diccionarios para ver como esta
    for camion_paquetes in orden_camiones:
        print(camion_paquetes)

    # Iterar sobre cada diccionario en la lista
    for diccionario in orden_camiones:
        # Obtener el nombre del camión y el diccionario de paquetes y coordenadas
        nombre_camion, paquetes_en_camion = list(diccionario.items())[0]
        
        # Coordenadas del almacén
        almacen = (42.359998, -71.058502)
        
        # Llamar a la función para encontrar la mejor ruta
        mejor_ruta, mejor_distancia = viajero_comercio(almacen, paquetes_en_camion)
        
        # Imprimir información sobre la ruta
        print(f"Camión {nombre_camion}:")
        print("Mejor ruta:", mejor_ruta)
        print("Distancia total:", mejor_distancia)
        
        # Dibujar la ruta
        dibujar_ruta(mejor_ruta, [almacen] + list(paquetes_en_camion.values()), mejor_distancia)

if __name__ == "__main__":
    main()
