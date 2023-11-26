import math
import matplotlib.pyplot as plt
import openpyxl
import geopandas as gpd
from shapely.geometry import Point

# Ruta al archivo Excel
#archivo_excel = ruta_archivo
def convertirdatos(flotante, flotante2, entero):
    convertido = False
    try:
        print(type(flotante))
        flotante=float(flotante)
        flotante=float(flotante2)
        flotante = int(entero)
    except:
        print("error")
        return convertido
    else:
        convertido = True
        return convertido

def archivoExcel(archivo_excel, nombreHoja, columnaC, columnaP,ultimaFila):
# Carga el libro de trabajo (workbook) 
    datosCosta = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    paquetes = {}
    contador = 1
    libro_trabajo = openpyxl.load_workbook(archivo_excel)
    coordenadas = []

    # Selecciona la hoja de trabajo (worksheet) por nombre
    hoja_trabajo = libro_trabajo[nombreHoja]

    # Especifica la letra de la columna que deseas (por ejemplo, 'A' para la columna A)
    ultimaFila = int(ultimaFila)
    # Itera sobre las primeras 20 filas de la columna deseada
    for fila in range(1, ultimaFila + 1):  # Empieza desde la fila 1 hasta la fila que se haya establecido
        celdaCoordenadas = f'{columnaC}{fila}'
        celdaPesos = f'{columnaP}{fila}'  # Construye la referencia de celda (por ejemplo, 'A1', 'A2', ...)
        valor_celdaCoordenadas = hoja_trabajo[celdaCoordenadas].value
        valor_celdaPesos = hoja_trabajo[celdaPesos].value
        
        if((valor_celdaPesos or valor_celdaCoordenadas != None)):
            x = ""
            y = ""
            segundoValor = False
            for i in valor_celdaCoordenadas:
                if i == ",":
                    segundoValor = True
                elif segundoValor == True:
                    y = y + i
                else:
                    x = x + i
            convertido =  convertirdatos(x,y,valor_celdaPesos)
            if convertido  != False:
                x=float(x)
                y=float(y)
                peso = int(valor_celdaPesos)
                punto = Point(y,x)
                enElMar =  not datosCosta.geometry.contains(punto).any()
                if enElMar == False:
                    if((-90 <= y <=90)and (-180 <= x <= 180)):
                        if(0<peso<=15):
                            coordenadas.append([])
                            coordenadas[contador-1].append(x)
                            coordenadas[contador-1].append(y)
                            paquetes[contador] = {"espacio":valor_celdaPesos, "coordenadas":(x,y)}
                            contador = contador+ 1


    return coordenadas, main(paquetes)
    # Cierra el libro de trabajo después de usarlo
    libro_trabajo.close()

#recibe el numero de camiones, el espacio de cada camión y la información de los paquetes sus coordenadas y peso de cada paquete
def organizar_paquetes(camiones, paquetes):
    # Ordenar los paquetes por espacio de menor a mayor
    paquetes_ordenados = sorted(paquetes.items(), key=lambda x: x[1]["espacio"])

    # Inicializar lista de resultado
    resultado = []
    
   
    while paquetes_ordenados:   #mientras haya paquetes
        for camion, capacidad in camiones.items(): #itera en la cantidad de camiones y su capacidad
            espacio_disponible = capacidad  #nombra a la capacidad como el espacio disponible para irlo restando
            paquetes_en_camion = {}         #declara un diccionario vacio para los paquetes que vayan a ir en el camión
    
            for paquete, info_paquete in paquetes_ordenados: #itera en el numero de paquetes que hay 
                if info_paquete["espacio"] <= espacio_disponible and paquete not in paquetes_en_camion: #Si el tamaño del paquete es menor o igual al espacio del camion y no se encuentra ya en el camión
                    paquetes_en_camion[paquete] = info_paquete["coordenadas"]   #Guarda ese paquete en el diccionario con sus respectivas coordenadas
                    espacio_disponible -= info_paquete["espacio"]   #se le resta al espacio disponible del camion el peso del paquete

            # Agregar a la lista de resultados solo si el diccionario no está vacío
            if paquetes_en_camion:
                resultado.append({camion: paquetes_en_camion})

            # Actualizar la lista de paquetes disponibles
            paquetes_ordenados = [(p, info) for p, info in paquetes_ordenados if p not in paquetes_en_camion]


    return resultado 

def distancia(punto1, punto2):#recibe dos puntos de entrega
    return math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2) #regresa la distancia que hay entre los puntos

def generar_rutas(almacen, clientes):    #recibe las coordenadas del almacen y las coordenadas de los clientes
    destinos = [almacen] + list(clientes.values())  
    num_destinos = len(destinos)    #el numero de destinos es igual al tamaño que tiene destinos
    visitados = [False] * num_destinos  
    ruta = [0]  # Comienza en el almacén
    visitados[0] = True 

    for _ in range(num_destinos - 1):   #itera en el rango del numero de destinos menos 1
        ciudad_actual = ruta[-1]        #
        distancia_minima = float('inf') #define la distancia minima como flotante infinito
        siguiente_ciudad = None         #define la siguiente ciudad como vacia

        for i in range(num_destinos):   #itera en el rando del numero de destinos
            if not visitados[i]:        #si no está visitada la ciudad 
                dist = distancia(destinos[ciudad_actual], destinos[i])  
                if dist < distancia_minima: #si la distancia actual es menor a la distancia minima
                    distancia_minima = dist #entonces la distancia actual se vuelve la nueva distancia minima
                    siguiente_ciudad = i    #

        ruta.append(siguiente_ciudad)   #a la ruta se le agrega la siguiente ciudad
        visitados[siguiente_ciudad] = True  #

    ruta.append(0)  #Al ultimo regresa al almacén al final

    distancia_total = sum(distancia(destinos[ruta[i]], destinos[ruta[i + 1]]) for i in range(num_destinos)) #la distancia total es la sumatoria de la distancia que hay entre cada destino de la ruta

    return ruta, distancia_total    #retorna la ruta y la distancia de esa ruta

"""
def dibujar_ruta(camino, destinos, mejor_distancia):    #para esta función recibe 
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
"""

def main(paquetes):
    contador = 0
    rutas = {}
    # Ejemplo de datos de entrada para la funcion de organizar paquetes
    camiones = {"camion1": 10, "camion2": 15}

    #paquetes = {
    #    "P1": {"espacio": 2, "coordenadas": (42.360613, -71.058556)},
    #    "P2": {"espacio": 7, "coordenadas": (42.361163, -71.057242)},
    #    "P3": {"espacio": 3, "coordenadas": (42.360200, -71.056934)},
    #    "P4": {"espacio": 5, "coordenadas": (42.359270, -71.057078)},
    #    "P5": {"espacio": 8, "coordenadas": (42.360350, -71.059055)}
    #}

    #paquetes = {
    #"P1": {"espacio": 15, "coordenadas": (42.360613, -71.058556)},
    #"P2": {"espacio": 10, "coordenadas": (42.361163, -71.057242)},
    #"P3": {"espacio": 15, "coordenadas": (42.360200, -71.056934)},
    #"P4": {"espacio": 10, "coordenadas": (42.359270, -71.057078)},
    #"P5": {"espacio": 15, "coordenadas": (42.360350, -71.059055)}
    #}

    # Ejemplo de datos de entrada para la ubicación del almacén
    almacen = (42.359998, -71.058502)

    # Obtener la lista con los diccionarios de cada camion
    orden_camiones = organizar_paquetes(camiones, paquetes)

    # Imprimir la lista de diccionarios para ver como esta
    print("\nLista de rutas")
    print("==================================")
    for camion_paquetes in orden_camiones:
        print(camion_paquetes)
    print("==================================")

    contador_ruta = 1

    for diccionario in orden_camiones:
        # Obtener el nombre del camión y el diccionario de paquetes y coordenadas
        nombre_camion, paquetes_en_camion = list(diccionario.items())[0]

        # Coordenadas del almacén
        almacen = (42.359998, -71.058502)

        # Llamar a la función para encontrar la mejor ruta
        mejor_ruta, mejor_distancia = generar_rutas(almacen, paquetes_en_camion)

        # Imprimir información sobre la ruta
        print(f"\nRuta {contador_ruta}")
        print(f"Vehiculo: {nombre_camion}")
        print(f"Paquetes: {paquetes_en_camion}")
        print("Mejor ruta:", mejor_ruta)
        print("Distancia total:", mejor_distancia)

        # Dibujar la ruta
        rutas[contador_ruta] = {"Ruta": mejor_ruta, "paquetes": paquetes_en_camion}
        contador_ruta += 1  # Incrementamos el contador de ruta
    
    
    return rutas