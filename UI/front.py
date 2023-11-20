from back import main

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkintermapview
coordenadas = []
root_tk = tk.Tk()
paquetes = {}
contador = 1

def app(root):

    root.title("Proyecto ADA")
    int_var = tk.IntVar()


    frame1 = tk.Frame(root, width = 400, height =600, bg="black")
    frame1.pack(side=tk.LEFT)
    frame1.pack_propagate(False)

    def quitarAdvetencia():
        labelAdvertencia_f1.config(text="")

    labelAdvertencia_f1 = tk.Label(frame1, text="", font=('Consolas', 12, 'bold'), fg='#f00',bg="black")
    labelAdvertencia_f1.place(relx= 0.5, rely=0.25,anchor="center")

    label1_f1 = tk.Label(frame1, text=" SmartDelivery", font=('Consolas', 20, 'bold'), fg='#f00',bg="black")
    label1_f1.place(relx= 0.5, rely=0.1,anchor="center")
    def datosM():
        if int_var.get() == 1:
            label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
            entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")
            label3_f1.place(relx= 0.5, rely=0.4, anchor="center")
            entry_label3_f1.place(relx= 0.5, rely=0.45, anchor="center")
            button_agregar_f1.place(relx= 0.5, rely=0.55,anchor="center")
        else:
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            label3_f1.place_forget()
            entry_label3_f1.place_forget()
            button_agregar_f1.place_forget()

    checkbutton_f1 = tk.Checkbutton(frame1,text="Datos de manera manual", variable=int_var, command=datosM, bg="black",fg="white")
    checkbutton_f1.place(relx= 0.5, rely=0.2,anchor="center")
    checkbutton_f1.select()

    label2_f1 = tk.Label(frame1, text=" Ingresa las cordenadas del punto de entrega",bg="black",fg="white")
    entry_label2_f1= tk.Entry(frame1, width=40)
    label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
    entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")

    label3_f1 = tk.Label(frame1, text=" Ingresa el peso del paquete",bg="black",fg="white")
    entry_label3_f1= tk.Entry(frame1, width=40)
    label3_f1.place(relx= 0.5, rely=0.4, anchor="center")
    entry_label3_f1.place(relx= 0.5, rely=0.45, anchor="center")

    def agregarMarcador():
        x = ""
        y = ""
        peso = entry_label3_f1.get()
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
            labelAdvertencia_f1.config(text="Dato incorrecto, revise la informacion")
            root.after(5000,quitarAdvetencia)
            print("Dato incorrecto")
        else:
            global contador
            contador= str(contador)
            nuevoMarcador = map_widget.set_marker(x,y, text="Punto"+contador)
            paquetes[contador] = {"espacio":peso, "coordenadas":(x,y)}
            contador = int(contador)
            contador = contador + 1
            coordenadas.append(nuevoMarcador)
            entry_label2_f1.delete(0, tk.END)
            entry_label3_f1.delete(0, tk.END)
        #markadorNuevo = map_widget.set_marker(entry_label2_f1.get())

    button_agregar_f1 = tk.Button(frame1, text="Agregar Punto", command=agregarMarcador)
    button_agregar_f1.place(relx= 0.5, rely=0.55,anchor="center")
   
    def abrir_explorador_archivos():                                                                #############################
        # Abre el diálogo de apertura de archivos
        ruta_archivo = filedialog.askopenfilename(title="Abrir archivo")  #ruta_archivo es la variable que contiene la ruta que debe ir a back para obtener las coordenadas y ponerlas en el mapa


    button_agregar_desde_archivo = tk.Button(frame1, text="Abrir Explorador de Archivos", command=abrir_explorador_archivos) ######
    button_agregar_desde_archivo.place(relx= 0.5, rely=0.75,anchor="center")                                                 ######

    labelh = tk.Label(frame1, text="Ingresa el nombre de la hoja donde se obtienen las coordenadas",bg="black",fg="white")  #######
    entry_labelh= tk.Entry(frame1, width=40)                                                                                #######
    labelh.place(relx= 0.5, rely=0.8, anchor="center")                                                                      #######
    entry_labelh.place(relx= 0.5, rely=0.85, anchor="center")                                                               #######
    #button_agregar_h = tk.Button(frame1, text="Introducir Nombre de hoja", command=Enviar_n_hoja)
    #button_agregar_h.place(relx= 0.5, rely=0.55,anchor="center")

    def empezarRuta():
        if(len(coordenadas)<2):
            labelAdvertencia_f1.config(text="No se han agregado coordenadas")
            root.after(5000,quitarAdvetencia)
        else:
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            label3_f1.place_forget()
            entry_label3_f1.place_forget()
            button_agregar_f1.place_forget()
            checkbutton_f1.place_forget()
            coordenadasO = []
            coordenadasO.append(almacen)
            rutas = main(paquetes)
            for ruta  in rutas:
                for i in ruta:
                    if i!=0 :
                        coordenadasO.append(coordenadas[i])
                coordenadasO.append(almacen)
                crearRuta = map_widget.set_path([elemento.position for elemento in coordenadasO])
                


    button_empezar_f1 = tk.Button(frame1, text="Empezar Ruta", command=empezarRuta)
    button_empezar_f1.place(relx= 0.5, rely=0.65,anchor="center")


    frame2 = tk.Frame(root, width = 800, height =600)
    frame2.pack()
    # create map widget

    map_widget = tkintermapview.TkinterMapView(frame2, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor="center")

    map_widget.set_position(20.66699813716904, -103.34871858245586) 
    map_widget.set_zoom(12.5)

    almacen = map_widget.set_marker(20.6573683, -103.3249406, text="Almacen")
    coordenadas.append(almacen)

    root.mainloop()

app(root_tk)
