
import tkinter as tk
from tkinter import ttk
import tkintermapview
coordenadas = []
root_tk = tk.Tk()

def app(root):
    root.title("Proyecto ADA")
    int_var = tk.IntVar()


    frame1 = tk.Frame(root, width = 400, height =600, bg="black")
    frame1.pack(side=tk.LEFT)
    frame1.pack_propagate(False)

    label1_f1 = tk.Label(frame1, text=" SmartDelivery", font=('Consolas', 20, 'bold'), fg='#f00',bg="black")
    label1_f1.place(relx= 0.5, rely=0.1,anchor="center")
    def datosM():
        if int_var.get() == 1:
            label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
            entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")
            button_agregar_f1.place(relx= 0.5, rely=0.41,anchor="center")
        else:
            label2_f1.place_forget()
            entry_label2_f1.place_forget()
            button_agregar_f1.place_forget()

    checkbutton_f1 = tk.Checkbutton(frame1,text="Datos de manera manual", variable=int_var, command=datosM, bg="black",fg="white")
    checkbutton_f1.place(relx= 0.5, rely=0.2,anchor="center")
    checkbutton_f1.select()

    label2_f1 = tk.Label(frame1, text=" Ingresa las cordenadas de los diferentes puntos:",bg="black",fg="white")
    entry_label2_f1= tk.Entry(frame1, width=40)
    label2_f1.place(relx= 0.5, rely=0.3, anchor="center")
    entry_label2_f1.place(relx= 0.5, rely=0.35, anchor="center")

    def agregarMarcador():
        x = ""
        y = ""
        segundoValor = False
        for i in entry_label2_f1.get():
            print(i)
            if i == ",":
                print(x)
                segundoValor = True
            elif segundoValor == True:
                y = y + i
            else:
                x = x + i
        try:
            x = float(x)
            y = float(y)
        except:
            print("no es un flotante")
        else:
            nuevoMarcador = map_widget.set_marker(x,y)
            coordenadas.append(nuevoMarcador)
            entry_label2_f1.delete(0, tk.END)
        #markadorNuevo = map_widget.set_marker(entry_label2_f1.get())

    button_agregar_f1 = tk.Button(frame1, text="Agregar Punto", command=agregarMarcador)
    button_agregar_f1.place(relx= 0.5, rely=0.41,anchor="center")
   
    def empezarRuta():
        ruta = map_widget.set_path([elemento.position for elemento in coordenadas])


    button_empezar_f1 = tk.Button(frame1, text="Empezar Ruta", command=empezarRuta)
    button_empezar_f1.place(relx= 0.5, rely=0.5,anchor="center")



    frame2 = tk.Frame(root, width = 800, height =600)
    frame2.pack()
    # create map widget

    map_widget = tkintermapview.TkinterMapView(frame2, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor="center")

    map_widget.set_position(20.66699813716904, -103.34871858245586) 
    map_widget.set_zoom(12.5)


    root.mainloop()

app(root_tk)