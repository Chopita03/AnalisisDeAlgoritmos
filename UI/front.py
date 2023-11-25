from back import main
from back import archivoExcel
import geopandas as gpd
from shapely.geometry import Point
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkintermapview
import random

coordenadas = []
root_tk = tk.Tk()
paquetes = {}
contador = 1
ruta_archivo = ""
colores = ["green", "black", "white", "red", "blue", "orange", "purple", "yellow", "pink", "cyan","gray"] 
lista = []
def app(root):

    root.title("Proyecto ADA")
    mostrar = tk.IntVar()

    def cerrarPrograma():
        root.destroy()
    def eliminarDatosFrames(opcionMenu):
        if(opcionMenu == "datosManual"):
            button_agregar_desde_archivo.place_forget() 
            label4_f1.place_forget() 
            entry_label4_f1.place_forget()
            button_eliminar_f1.place_forget()
            labelh.place_forget()
            entry_labelh.place_forget()
            labelh2.place_forget()
            labelh3.place_forget()
            entry_labelh.place_forget()
            entry_labelh2.place_forget()
            entry_labelh3.place_forget()
            button_empezarA_f1.place_forget()
            entry_labelh4.place_forget()
            button_empezarA_f1.place_forget()
            
            
        elif(opcionMenu == "datosAutomatico"):
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            label3_f1.place_forget()
            entry_label3_f1.place_forget()
            button_agregar_f1.place_forget()
            label4_f1.place_forget() 
            entry_label4_f1.place_forget()
            button_eliminar_f1.place_forget()
            button_empezar_f1.place_forget()
            label3_1_f1.place_forget()
            entry_label3_1_f1.place_forget()
            
        elif(opcionMenu == "eliminarMarcador"):
            button_agregar_desde_archivo.place_forget()
            labelh.place_forget()
            entry_labelh.place_forget() 
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            label3_f1.place_forget()
            entry_label3_f1.place_forget()
            button_agregar_f1.place_forget()
            button_empezar_f1.place_forget()
            labelh2.place_forget()
            entry_labelh2.place_forget() 
            labelh3.place_forget() 
            entry_labelh3.place_forget() 
            button_empezarA_f1.place_forget()
            label3_1_f1.place_forget()
            entry_label3_1_f1.place_forget()
            entry_labelh4.place_forget()
            button_empezarA_f1.place_forget()

        frame3.lower(frame1)  
        mostrar.set(0)

    def mostrarMenu():
        nuevo_estado = 1 - mostrar.get()
        mostrar.set(nuevo_estado)
        if(mostrar.get() == 0):
            frame3.lower(frame1)
        else:
            frame3.lift(frame1)

    def quitarAdvetencia():
        labelAdvertencia_f1.config(text="")

    def datosManual():
        eliminarDatosFrames("datosManual")
        label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
        entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")
        label3_f1.place(relx= 0.5, rely=0.4, anchor="center")
        entry_label3_f1.place(relx= 0.5, rely=0.45, anchor="center")
        button_empezar_f1.place(relx= 0.5, rely=0.65,anchor="center")
        label3_1_f1.place(relx= 0.5, rely=0.5, anchor="center")
        entry_label3_1_f1.place(relx= 0.5, rely=0.55, anchor="center")
        button_agregar_f1.place(relx= 0.5, rely=0.63,anchor="center")
        button_empezar_f1.place(relx= 0.5, rely=0.7,anchor="center")
        

    def datosAutomatico():
        eliminarDatosFrames("datosAutomatico")
        button_agregar_desde_archivo.place(relx= 0.5, rely=0.3,anchor="center")     
        labelh.place(relx= 0.5, rely=0.35, anchor="center")                                                                   #######
        entry_labelh.place(relx= 0.5, rely=0.4, anchor="center") 
        labelh2.place(relx= 0.5, rely=0.45, anchor="center") 
        entry_labelh2.place(relx= 0.5, rely=0.5, anchor="center") 
        labelh3.place(relx= 0.5, rely=0.55, anchor="center") 
        entry_labelh3.place(relx= 0.5, rely=0.6, anchor="center")
        labelh4.place(relx= 0.5, rely=0.65, anchor="center")
        entry_labelh4.place(relx= 0.5, rely=0.70, anchor="center")
        button_empezarA_f1.place(relx= 0.5, rely=0.75,anchor="center")

    def eliminarMarcador():
        eliminarDatosFrames("eliminarMarcador")
        label4_f1.place(relx= 0.5, rely=0.4, anchor="center")
        entry_label4_f1.place(relx= 0.5, rely=0.45, anchor="center")
        button_eliminar_f1.place(relx= 0.5, rely=0.52, anchor="center")

    def abrir_explorador_archivos():                                                                #############################
        # Abre el diálogo de apertura de archivos
        global  ruta_archivo 
        ruta_archivo = filedialog.askopenfilename(title="Abrir archivo") #ruta_archivo es la variable que contiene la ruta que debe ir a back para obtener las coordenadas y ponerlas en el mapa
        if(ruta_archivo.endswith(".xlsx") == True):
            labelAdvertencia_f1.config(text="Archivo '.xlsx' agregado exitosamente",fg= "#66e125" )
            root.after(5000,quitarAdvetencia)
        else:
            labelAdvertencia_f1.config(text="El archivo no es de formato '.xlsx'",fg='#f00')
            root.after(5000,quitarAdvetencia)
     
    def empezarRutaAutomatica():
       
        contadorDestino = 1
        numero_aleatorio = random.randint(0, 10)
        global contador
        coordenadasO = []
        coordenadasO.append(almacen.position)
        x = 0
        y = 0
        try:
            coordenadasD, rutas = archivoExcel(ruta_archivo, entry_labelh.get(), entry_labelh2.get(),entry_labelh3.get(),entry_labelh4.get())
        except:
            labelAdvertencia_f1.config(text="Error en los datos ingresados, intende de nuevo'",fg='#f00')
            root.after(5000,quitarAdvetencia)
            
        else:
            print(coordenadasD)
            for i in range(len(coordenadasD)):
                x=coordenadasD[i][0]
                y=coordenadasD[i][1]
                contador = str(contador)
                nuevoMarcador = map_widget.set_marker(x,y, text="Marcador" + contador)
                contador = int(contador)
                coordenadas.append(nuevoMarcador)
                contador = contador + 1
            contador = 1
            for i in range(len(rutas)):
                numero_aleatorio = random.randint(0, 10)
                for ruta in rutas[i+1]["Ruta"]:
                    if ruta != 0:
                        contador = 1
                        for paquete in rutas[i+1]["paquetes"]:
                            if ruta == contador:
                                coordenadasO.append(rutas[i+1]["paquetes"][paquete])
                                contadorDestino = str(contadorDestino)
                                coordenadas[paquete].set_text(coordenadas[paquete].text + "\n" + "Destino N°"+contadorDestino)
                                contadorDestino = int(contadorDestino)
                                contadorDestino = contadorDestino + 1
                            contador = contador+ 1
                        print(ruta, rutas[i+1]["paquetes"])
                coordenadasO.append(almacen.position)
                crearRuta = map_widget.set_path([elemento for elemento in coordenadasO],color=colores[numero_aleatorio])
                coordenadasO = []
                contadorDestino = 1
                coordenadasO.append(almacen.position)
            button_agregar_desde_archivo.place_forget()
            labelh.place_forget()
            entry_labelh.place_forget()
            labelh2.place_forget()
            labelh3.place_forget()
            entry_labelh.place_forget()
            entry_labelh2.place_forget()
            entry_labelh3.place_forget()
            button_empezarA_f1.place_forget()
            button1_f3.place_forget()
            button2_f3.place_forget()
            button3_f3.place_forget()
            labelh4.place_forget()
            entry_labelh4.place_forget()
            label5_f1.place(relx= 0.5, rely=0.3, anchor="center")
            button1_label5_f1.place(relx= 0.5, rely=0.37, anchor="center")
            button2_label5_f1.place(relx= 0.5, rely=0.44, anchor="center")

    def agregarMarcador():
        peso = entry_label3_f1.get()
        punto = 0
        datosCosta = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
        x = ""
        y = ""
        segundoValor = False
        for i in entry_label2_f1.get():
            if i == ",":
                segundoValor = True
            elif segundoValor == True:
                y = y + i
            else:
                x = x + i
        try:
            peso = int(peso)
            x = float(x)
            y = float(y)
        except:
            labelAdvertencia_f1.config(text="Dato incorrecto, revise la informacion",fg='#f00')
            root.after(5000,quitarAdvetencia)
            print("Dato incorrecto")
        else:
            if((-90 <= y <=90)and (-180 <= x <= 180)):
                if((peso > 15) or (peso <= 0)):
                    labelAdvertencia_f1.config(text="Peso del paquete incorrecto, intente de nuevo",fg='#f00')
                    root.after(5000,quitarAdvetencia)
                    return
                punto = Point(y,x)
                enElMar =  not datosCosta.geometry.contains(punto).any()
                if enElMar:
                    print("no se puede agregar el dato") 
                    labelAdvertencia_f1.config(text="Las coordenadas estan en el mar, intente de nuevo",fg='#f00')
                    root.after(5000,quitarAdvetencia)
                else:
                    global contador
                    if(entry_label3_1_f1.get() == ""):
                        contador = str(contador)
                        nombre = ("Marcador" + contador)
                        contador = int(contador)
                    else:
                        nombre = entry_label3_1_f1.get()
                        for i in coordenadas:
                            if nombre  == i[2]:
                                labelAdvertencia_f1.config(text="Ya existe un marcador con ese nombre,\n intente de nuevo",fg='#f00')
                                root.after(5000,quitarAdvetencia)
                                return
                    
                    nuevoMarcador = map_widget.set_marker(x,y, text=nombre)
                    #paquetes[contador] = {"espacio":peso, "coordenadas":(x,y)}
                    coordenadas.append([])
                    coordenadas[contador].append(nuevoMarcador)
                    coordenadas[contador].append(peso)
                    coordenadas[contador].append(nombre)
                    coordenadas[contador].append(x)
                    coordenadas[contador].append(y)
                    nuevoMarcador = 0
                    contador = contador + 1
                    entry_label2_f1.delete(0, tk.END)
                    entry_label3_f1.delete(0, tk.END)
                    entry_label3_1_f1.delete(0, tk.END)
                    print(coordenadas)
                    labelAdvertencia_f1.config(text="Marcador agregado exitosamente",fg= "#66e125" )
                    root.after(5000,quitarAdvetencia)
            else:
                labelAdvertencia_f1.config(text="Error en las coordenadas, intente de nuevo",fg='#f00')
                root.after(5000,quitarAdvetencia)
        #markadorNuevo = map_widget.set_marker(entry_label2_f1.get())
    
    def eliminar():
        global contador
        print(coordenadas)
        nombre  = entry_label4_f1.get()
        if(nombre == "Almacen"):
            labelAdvertencia_f1.config(text="No se puede eliminar el Almacen",fg='#f00')
            root.after(5000,quitarAdvetencia)
        else:
            for i in range(len(coordenadas)):
                if coordenadas[i][2] == nombre:
                    coordenadas[i][0].delete()
                    coordenadas.pop(i)
                    labelAdvertencia_f1.config(text="Marcador eliminado exitosamente",fg= "#66e125" )
                    root.after(5000,quitarAdvetencia)
                    contador = contador - 1
                    return
            labelAdvertencia_f1.config(text="No existe un marcador con ese nombre",fg='#f00')
            root.after(5000,quitarAdvetencia)


    def empezarRuta():
        contadorDestino = 1
        nombre = "dawdawdawdawd"
        print(coordenadas, "Zorrita")
        if(len(coordenadas)<2):
            labelAdvertencia_f1.config(text="No se han agregado coordenadas",fg='#f00')
            root.after(5000,quitarAdvetencia)
        else:
            global contador
            contador = 1
            label3_1_f1.place_forget()
            entry_label3_1_f1.place_forget()
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            label3_f1.place_forget()
            entry_label3_f1.place_forget()
            button_agregar_f1.place_forget()
            button1_f3.place_forget()
            button2_f3.place_forget()
            button3_f3.place_forget()
            button_empezar_f1.place_forget()
            coordenadasO = []
            coordenadasO.append(almacen.position)
            for i in range(len(coordenadas)):
                if i !=0:
                    print(coordenadas[i])
                    paquetes[contador] = {"espacio":coordenadas[i][1], "coordenadas":(coordenadas[i][3],coordenadas[i][4])}
                    contador = contador + 1 
            rutas = main(paquetes)
            contador = 1
            for i in range(len(rutas)):
                numero_aleatorio = random.randint(0, 10)
                for ruta in rutas[i+1]["Ruta"]:
                    if ruta != 0:
                        contador = 1
                        for paquete in rutas[i+1]["paquetes"]:
                            if ruta == contador:
                                coordenadasO.append(rutas[i+1]["paquetes"][paquete])
                                contadorDestino = str(contadorDestino)
                                coordenadas[paquete][0].set_text(coordenadas[paquete][0].text + "\n" + "Destino N°"+contadorDestino)
                                contadorDestino = int(contadorDestino)
                                contadorDestino = contadorDestino + 1
                            contador = contador+ 1
                        print(ruta, rutas[i+1]["paquetes"])
                coordenadasO.append(almacen.position)
                crearRuta = map_widget.set_path([elemento for elemento in coordenadasO],color=colores[numero_aleatorio])
                coordenadasO = []
                contadorDestino = 1
                coordenadasO.append(almacen.position)
            label5_f1.place(relx= 0.5, rely=0.3, anchor="center")
            button1_label5_f1.place(relx= 0.5, rely=0.37, anchor="center")
            button2_label5_f1.place(relx= 0.5, rely=0.44, anchor="center")
            
    def nuevasRutas():
        global coordenadas, almacen, contador, paquetes
        paquetes = {}
        label5_f1.place_forget()
        button1_label5_f1.place_forget()
        button2_label5_f1.place_forget()
        label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
        entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")
        label3_f1.place(relx= 0.5, rely=0.4, anchor="center")
        entry_label3_f1.place(relx= 0.5, rely=0.45, anchor="center")
        button_empezar_f1.place(relx= 0.5, rely=0.65,anchor="center")
        label3_1_f1.place(relx= 0.5, rely=0.5, anchor="center")
        entry_label3_1_f1.place(relx= 0.5, rely=0.55, anchor="center")
        button_agregar_f1.place(relx= 0.5, rely=0.63,anchor="center")
        button_empezar_f1.place(relx= 0.5, rely=0.7,anchor="center")
        contador = 1
        map_widget.delete_all_path()
        try:
            for i in range(len(coordenadas)) :
                if i != 0:
                    coordenadas[i].delete()
        except:
            for datos in coordenadas:
                datos[0].delete()
            coordenadas = []
            almacen = map_widget.set_marker(20.6573683, -103.3249406, text="Almacen")
            coordenadas.append([])
            coordenadas[0].append(almacen)
            coordenadas[0].append(0)
            coordenadas[0].append("Almacen")
            button1_f3.place(relx= 0.5, rely=0.2,anchor="center")
            button2_f3.place(relx= 0.5, rely=0.3,anchor="center")
            button3_f3.place(relx= 0.5, rely=0.4,anchor="center")
        else:
            almacen = map_widget.set_marker(20.6573683, -103.3249406, text="Almacen")
            coordenadas = []
            coordenadas.append([])
            coordenadas[0].append(almacen)
            coordenadas[0].append(0)
            coordenadas[0].append("Almacen")
            button1_f3.place(relx= 0.5, rely=0.2,anchor="center")
            button2_f3.place(relx= 0.5, rely=0.3,anchor="center")
            button3_f3.place(relx= 0.5, rely=0.4,anchor="center")
        

    #Codigo del Frame1 (Accion a ejecutar ----------------------------------------------------------------)
    frame1 = tk.Frame(root, width = 400, height =600, bg="black")
    frame1.pack(side=tk.LEFT)
    frame1.pack_propagate(False)

    button_f1_menu = tk.Button(root,text="≡", width = 5, height =2, bg="white", pady=0, font = ("Arial", 12), command=mostrarMenu)
    button_f1_menu.place(relx= 0, rely=0)

    labelAdvertencia_f1 = tk.Label(frame1, text="", font=('Consolas', 12, 'bold'), fg='#f00',bg="black")
    labelAdvertencia_f1.place(relx= 0.5, rely=0.25,anchor="center")

    label1_f1 = tk.Label(frame1, text=" SmartDelivery", font=('Consolas', 20, 'bold'), fg='#f00',bg="black")
    label1_f1.place(relx= 0.5, rely=0.1,anchor="center")

    label2_f1 = tk.Label(frame1, text=" Ingresa las cordenadas del punto de entrega",bg="black",fg="white")
    entry_label2_f1= tk.Entry(frame1, width=40)
    label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
    entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")

    label3_f1 = tk.Label(frame1, text=" Ingresa el peso del paquete",bg="black",fg="white")
    entry_label3_f1= tk.Entry(frame1, width=40)
    label3_f1.place(relx= 0.5, rely=0.4, anchor="center")
    entry_label3_f1.place(relx= 0.5, rely=0.45, anchor="center")

    label3_1_f1 = tk.Label(frame1, text=" Nombre del marcador",bg="black",fg="white")
    label3_1_f1.place(relx= 0.5, rely=0.5, anchor="center")

    entry_label3_1_f1 = tk.Entry(frame1, width=40)
    entry_label3_1_f1.place(relx= 0.5, rely=0.55, anchor="center")

    button_agregar_f1 = tk.Button(frame1, text="Agregar Punto", command=agregarMarcador)
    button_agregar_f1.place(relx= 0.5, rely=0.63,anchor="center")

    button_agregar_desde_archivo = tk.Button(frame1, text="Abrir Explorador de Archivos", command=abrir_explorador_archivos) ######                                                 ######

    labelh = tk.Label(frame1, text="Ingresa el nombre de la hoja donde se obtienen las coordenadas",bg="black",fg="white")  #######
    labelh2 = tk.Label(frame1, text="Ingresa el nombre de la columna de las cordenadas",bg="black",fg="white")
    labelh3 = tk.Label(frame1, text="Ingresa el nombre de la columna de los pesos",bg="black",fg="white")
    labelh4 = tk.Label(frame1, text="Ingresa el nombre de la ultima fila donde se encuentren datos",bg="black",fg="white")

    entry_labelh= tk.Entry(frame1, width=40)
    entry_labelh2= tk.Entry(frame1, width=40)  
    entry_labelh3= tk.Entry(frame1, width=40)
    entry_labelh4= tk.Entry(frame1, width=40)        
         
    
    button_empezarA_f1 = tk.Button(frame1, text="Empezar Ruta", command=empezarRutaAutomatica)                                                                 #######                                                             #######
    #button_agregar_h = tk.Button(frame1, text="Introducir Nombre de hoja", command=Enviar_n_hoja)
    #button_agregar_h.place(relx= 0.5, rely=0.55,anchor="center")
                
    button_empezar_f1 = tk.Button(frame1, text="Empezar Ruta", command=empezarRuta)
    button_empezar_f1.place(relx= 0.5, rely=0.7,anchor="center")

    label4_f1 = tk.Label(frame1, text=" Ingresa el numero de marcador a eliminar",bg="black",fg="white")
    entry_label4_f1 = tk.Entry(frame1, width=40)
    button_eliminar_f1 = tk.Button(frame1, text="Eliminar", command=eliminar)

    label5_f1 = tk.Label(frame1, text=" ¿Deseas iniciar una nueva ruta?",bg="black",fg="white")
    button1_label5_f1 = tk.Button(frame1, text="Nueva ruta", command = nuevasRutas)
    button2_label5_f1 = tk.Button(frame1, text="Cerrar programa", command=cerrarPrograma)
    #Codigo del Frame2 (MAPA----------------------------------------------------------------)
    frame3 = tk.Frame(root, width = 200, height =600, bg="blue")
    frame2 = tk.Frame(root, width = 800, height =600)
    frame2.pack()

    map_widget = tkintermapview.TkinterMapView(frame2, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor="center")

    map_widget.set_position(20.66699813716904, -103.34871858245586) 
    map_widget.set_zoom(12.5)

    almacen = map_widget.set_marker(20.6573683, -103.3249406, text="Almacen")
    coordenadas.append([])
    coordenadas[0].append(almacen)
    coordenadas[0].append(0)
    coordenadas[0].append("Almacen")

    #Codigo del Frame3 (menu de opciones ----------------------------------------------------------------)
    frame3 = tk.Frame(root, width = 200, height =600, bg="white")
    frame3.pack(side=tk.LEFT)
    frame3.lower(frame1)
    frame3.place(relx= 0)

    button1_f3 = tk.Button(frame3,text="Datos de manera manual", bg="gray",fg="white",width = 200, height =3, command=datosManual)
    button1_f3.place(relx= 0.5, rely=0.2,anchor="center")
    
    button2_f3 = tk.Button(frame3,text="Datos de manera automatica", bg="gray",fg="white",width = 200, height =3, command=datosAutomatico)
    button2_f3.place(relx= 0.5, rely=0.3,anchor="center")

    button3_f3 = tk.Button(frame3,text="Eliminar un marcador", bg="gray",fg="white",width = 200, height =3,  command=eliminarMarcador)
    button3_f3.place(relx= 0.5, rely=0.4,anchor="center")

    button4_f3 = tk.Button(frame3,text="Empezar una ruta nueva", bg="gray",fg="white",width = 200, height =3, command = nuevasRutas)
    button4_f3.place(relx= 0.5, rely=0.5,anchor="center")

    button5_f3 = tk.Button(frame3,text="Cerrar Programa", bg="gray",fg="white",width = 200, height =3, command=cerrarPrograma)
    button5_f3.place(relx= 0.5, rely=0.6,anchor="center")
    # create map widget
    root.mainloop()


app(root_tk)
