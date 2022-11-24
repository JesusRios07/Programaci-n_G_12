from tkinter import *
from PIL import ImageTk, Image
import sys
import json
import os
#import pandas as pd

#Funciones del código
def eliminar():
    if nombre_articulo in nombres:
        indice = nombres.index(nombre_articulo)
        del nombres[indice]
        del precios[indice]
        del cantidades_vendidas[indice]
        Borra=Label(marco8,text=f"Se eliminó {nombre_articulo}",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="red").place(x=130,y=250)
    else:
        marco9.tkraise()
        print("No se encuentra el articulo en inventario.")

def registro_ven():
    if nombre_articulo in nombres:
        indice = nombres.index(nombre_articulo)
        precio = precios[indice]
        cantidades_vendidas[indice] += cantidad
        cantida_v= Label(marco6,text=f"Se vende(venden) {cantidad} {nombre_articulo}. Total: {cantidad * precio}",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="green",cursor='hand1').place(x=50,y=250)
    else:
        marco9.tkraise()#Muestra marco 9 por error
        print("Artículo no existe")


def balance():
    if len(data_articulos["inventario"]) <= 0:
        vacio=Label(marco7,text="No hay artículos agregados al carrito",bg="red",relief="flat",font=("Public Sans",10,"bold"),fg="#230871").place(x=150,y=300)
    tabla_1=Label(marco7,text="+--------------------+----------+----------+----------+",bg="green",font=("Public Sans",8,"bold")).place(x=30,y=90)
    tabla_2=Label(marco7,text="|NOMBRE              |CANT.     |PRECIO    |IMPORTE   |",bg="green",font=("Public Sans",8,"bold")).place(x=150,y=110)
    tabla_2=Label(marco7,text="+--------------------+----------+----------+----------+",bg="green",font=("Public Sans",8,"bold")).place(x=150,y=110)
    indice = 0
    total = 0
    for articulo in data_articulos["inventario"]:
        importe = articulo["precio"] * articulo["cantidades_vendidas"]
        orden=Label(marco7,text="|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
            articulo["nombre"], articulo["cantidades_vendidas"], articulo["precio"], importe),bg="green",font=("Public Sans",8,"bold")).place(x=30,y=90)
        superior=Label(marco7,text="+--------------------+----------+----------+----------+",bg="green",font=("Public Sans",8,"bold")).place(x=30,y=100)
        total += importe
            #indice += 1
    tabla_b_1=Label(marco7,text=
            "|--------------------|----------|TOTAL:    |{:>10.2f}|".format(total),bg="green",font=("Public Sans",8,"bold")).place(x=30,y=90)
    tabla_b_2=Label(marco7,text="+--------------------+----------+----------+----------+",bg="green",font=("Public Sans",8,"bold")).place(x=30,y=110)

def sig_1():
    print("el marco uno ha sido ocultado ")
    marco2.tkraise()#mostrar el marco 2
    print("el marco dos ha sido mostrado ")

def sig_2():
    print("el marco dos ha sido ocultado ")
    marco3.tkraise()#mostrar el marco 3
    print("el marco tres ha sido mostrado ")

def sig_3():
    print("el marco dos ha sido ocultado ")
    marco4.tkraise()#mostrar el marco 4
    usu_1=usuario.get()
    Bienvenida_usu=Label(marco4,text=f"{usu_1}",bg="#230871",relief="flat", font=("Montserrat Classic",14,"bold"),fg="white").place(x=150,y=25)
    print("el marco cuatro ha sido mostrado ")

def sig_4():
    print("el marco tres ha sido ocultado ")
    marco2.tkraise()#mostrar el marco 2
    print("el marco dos ha sido mostrado ")

def sig_5():
    print("el marco cuatro ha sido ocultado ")
    marco5.tkraise()#mostrar el marco 5
    print("el marco cinco ha sido mostrado ")

def sig_6():
    print("el marco cuatro ha sido ocultado ")
    marco6.tkraise()#mostrar el marco 6
    print("el marco seis ha sido mostrado ")

def sig_7():
    print("el marco cuatro ha sido ocultado ")
    marco7.tkraise()#mostrar el marco 7
    print("el marco siete ha sido mostrado ")

def sig_8():
    print("el marco cuatro ha sido ocultado ")
    marco8.tkraise()#mostrar el marco 8
    print("el marco ocho ha sido mostrado ")

def atras_1():
    print("el marco cinco ha sido ocultado ")
    try:
        cantidad_vendida = 0.0
        nombres.append(nombre)
        precios.append(precio)
        cantidades_vendidas.append(cantidad_vendida)
        data_articulos["inventario"].append({"nombre": nombre, "precio": precio, "cantidades_vendidas": cantidad_vendida})
    except:
        print("Archivo json no iniciado")
    nombre_art.set(" ")#Limpiar entrada
    marco4.tkraise()#mostrar el marco 4
    print("el marco cuatro ha sido mostrado ")

def atras_2():
    print("el marco seis ha sido ocultado ")
    nombre_cont.set(" ")
    marco4.tkraise()#mostrar el marco 4
    print("el marco cuatro ha sido mostrado ")

def atras_3():
    print("el marco siete ha sido ocultado ")
    marco4.tkraise()#mostrar el marco 4
    print("el marco cuatro ha sido mostrado ")

def atras_4():
    print("el marco ocho ha sido ocultado ")
    borrar_1.set(" ")
    marco4.tkraise()#mostrar el marco 4
    print("el marco cuatro ha sido mostrado ")

def atras_5():
    print("el marco cuatro ha sido ocultado ")
    marco2.tkraise()#mostrar el marco 2
    print("el marco dos ha sido mostrado ")

def atras_6():
    print("el marco nueve ha sido ocultado ")
    marco8.tkraise()#mostrar el marco 8
    print("el marco ocho ha sido mostrado ")

def salida(): 
    raiz.destroy()

raiz=Tk()
raiz.title('Interfaz de usuario_1')
raiz.configure(height='400',width='450')
raiz.geometry("454x404+500+50")
raiz.configure(bg='dark blue')


inventario = {"inventario": []}
#Archivo json deben crearlo con el Drive de cada usuario
#C_V = open("/content/drive/MyDrive/Colab Notebooks/codigo_proyecto.json", "r")
#print(C_V.read())

#C_V = open("/content/drive/MyDrive/Colab Notebooks/codigo_proyecto.json", "r")

#data_articulos =json.load(C_V.read())

#Variables
data_articulos ={}
control_de_ventas = {}
nombres = []
precios = []
cantidades_vendidas = []

#Marco 9
marco9=Frame(raiz)
marco9.pack()
marco9.grid_propagate(False)
marco9.place_configure(x=0,y=0)
marco9.configure(bg='dark blue')
#Fondo 9
image_8=Image.open("Error.png")
image_8=image_8.resize((450,400),Image.ANTIALIAS)
img_8=ImageTk.PhotoImage(image_8)
img_p8=Label(marco9, image=img_8)
img_p8.pack()
#Anuncio
Err_1=Label(marco9,text="!Error!",bg="white",relief="flat",font=("Public Sans",8,"bold")).place(x=200,y=50)
Err_2=Label(marco9,text="¡Error! \nArtículo no se encuentra \no \nhay error de digitación",bg="#3effe6",relief="flat",font=("Public Sans",15,"bold"),fg="red").place(x=105,y=200)
#Boton
inventario_3=Button(marco9,text="I",command=atras_6,bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


#Marco 8
marco8=Frame(raiz)
marco8.pack()
marco8.grid_propagate(False)
marco8.place_configure(x=0,y=0)
marco8.configure(bg='dark blue')
#Fondo 8
image_7=Image.open("Borrar.png")
image_7=image_7.resize((450,400),Image.ANTIALIAS)
img_7=ImageTk.PhotoImage(image_7)
img_p7=Label(marco8, image=img_7)
img_p7.pack()
#Entrada y boton
ren_m6_1=Label(marco8,text="Ingrese artículo",bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),fg="#230871").place(x=150,y=165)
borrar_1=StringVar()
art_borrar=Entry(marco8,textvariable=borrar_1,relief="flat",font=("Public Sans",8,"bold")).place(x=150,y=192)
Borrador=Button(marco8,text="Borrar",command=eliminar,bg="red",relief="flat",font=("Public Sans",10,"bold"),fg="#230871",cursor='hand1').place(x=190,y=61)
#Boton
inventario_3=Button(marco8,text="I",command=atras_4,bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


#Marco 7
marco7=Frame(raiz)
marco7.pack()
marco7.grid_propagate(False)
marco7.place_configure(x=0,y=0)
marco7.configure(bg='dark blue')
#Fondo 7
image_6=Image.open("Informe.png")
image_6=image_6.resize((450,400),Image.ANTIALIAS)
img_6=ImageTk.PhotoImage(image_6)
img_p6=Label(marco7, image=img_6)
img_p6.pack()
#Línea
Balance_1=Button(marco7,text="Balance",command=balance,bg="white",relief="flat",font=("Public Sans",10,"bold"),cursor='hand1').place(x=190,y=28)
#Boton
inventario_2=Button(marco7,text="I",command=atras_3,bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


#Marco 6
marco6=Frame(raiz)
marco6.pack()
marco6.grid_propagate(False)
marco6.place_configure(x=0,y=0)
marco6.configure(bg='dark blue')
#Fondo 6
image_5=Image.open("Ventas.png")
image_5=image_5.resize((450,400),Image.ANTIALIAS)
img_5=ImageTk.PhotoImage(image_5)
img_p5=Label(marco6, image=img_5)
img_p5.pack()
#Entradas
ren_m6_2=Label(marco6,text="Ingrese artículo",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="#230871").place(x=180,y=165)
ren_m6_3=Label(marco6,text="Ingrese cantidad vendida",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="#230871").place(x=142,y=230)
nombre_cont=StringVar()
cantidad=DoubleVar()
nombre_articulo=Entry(marco6,textvariable=nombre_cont,relief="flat",font=("Public Sans",8,"bold")).place(x=140,y=192) 
cantidad_1=Entry(marco6,textvariable=cantidad,relief="flat",font=("Public Sans",8,"bold")).place(x=140,y=258) 
#Boton
informe=Button(marco6,text="Guardar",command=registro_ven,bg="green",relief="flat",font=("Public Sans",10,"bold"),fg="#230871",cursor='hand1').place(x=190,y=61)
inventario_1=Button(marco6,text="I",command=atras_2,bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


#Marco 5
marco5=Frame(raiz)
marco5.pack()
marco5.grid_propagate(False)
marco5.place_configure(x=0,y=0)
marco5.configure(bg='dark blue')
#Fondo 5
image_4=Image.open("Registro_de_artículo.png")
image_4=image_4.resize((450,400),Image.ANTIALIAS)
img_4=ImageTk.PhotoImage(image_4)
img_p4=Label(marco5, image=img_4)
img_p4.pack()
#Entradas
ren_m5_1=Label(marco5,text="Ingrese fecha",bg="#230871",relief="flat",font=("Public Sans",10,"bold"),fg="white").place(x=180,y=35)
ren_m5_2=Label(marco5,text="Ingrese artículo",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="#230871").place(x=180,y=165)
ren_m5_3=Label(marco5,text="Ingrese el precio",bg="#3effe6",relief="flat",font=("Public Sans",10,"bold"),fg="#230871").place(x=180,y=227)
fecha_inv=StringVar()
nombre_art=StringVar()
precios_art=DoubleVar()
fecha=Entry(marco5,textvariable=fecha_inv,relief="flat",font=("Public Sans",8,"bold")).place(x=180,y=65)
nombre=Entry(marco5,textvariable=nombre_art,relief="flat",font=("Public Sans",8,"bold")).place(x=140,y=192) 
precio=Entry(marco5,textvariable=precios_art,relief="flat",font=("Public Sans",8,"bold")).place(x=140,y=258) 
#Boton
Inventario_0=Button(marco5,text="I",command= atras_1,bg="#3effe6",relief="flat",font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


#Marco 4
marco4=Frame(raiz)
marco4.pack()
marco4.grid_propagate(False)
marco4.place_configure(x=0,y=0)
marco4.configure(bg='dark blue')
#Fondo 4
image_3=Image.open("Instrucciones.png")
image_3=image_3.resize((450,400),Image.ANTIALIAS)
img_3=ImageTk.PhotoImage(image_3)
img_p3=Label(marco4, image=img_3)
img_p3.pack()
#Bienvenida
Bienvenida=Label(marco4,text="¡Te damos la bienvenida a Control de Ventas!",bg="#230871",relief="flat", font=("Montserrat Classic",14,"bold"),fg="white").place(x=27,y=50)
#Contenido de Instruciones
Administración=Button(marco4,text="Admistración",command=atras_5,bg="white",relief="flat",font=("Monntserrat Classic",7,"bold"),cursor='hand1').place(x=195,y=90)
Titulo_Instr=Label(marco4,text="INSTRUCIONES\t\tOPCIÓN",bg="#230871",relief="flat", font=("Montserrat Classic",14,"bold"),fg="white").place(x=60,y=140)
Instruciones=Label(marco4,text="Introducir un artículo al inventario\n\n Ventas\t\t\t\t\n\n Mostrar información de ventas\t\n\n Borrar articulo del inventario\t",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=180)
#Cerrar sesión
Cerrar_sesion=Button(marco4,text="Cerrar sesión",bg="white",command=salida, relief="flat", font=("Montserrat Classic",7,"bold"),cursor='hand1').place(x=195,y=301)
#Botones de Instruciones
Opicion_1=Button(marco4,text="1",bg="#230871",command=sig_5,relief="flat",font=("Montserrat Classic",12,"bold"),cursor='hand1',fg="#3effe6").place(x=355,y=176)
Opicion_2=Button(marco4,text="2",bg="#230871",command=sig_6,relief="flat",font=("Montserrat Classic",12,"bold"),cursor='hand1',fg="#3effe6").place(x=355,y=203)
Opicion_3=Button(marco4,text="3",bg="#230871",command=sig_7,relief="flat",font=("Montserrat Classic",12,"bold"),cursor='hand1',fg="#3effe6").place(x=355,y=230)
Opicion_4=Button(marco4,text="4",bg="#230871",command=sig_8,relief="flat",font=("Montserrat Classic",12,"bold"),cursor='hand1',fg="#3effe6").place(x=355,y=257)

#Marco 3
marco3=Frame(raiz)
marco3.pack()
marco3.grid_propagate(False)
marco3.place_configure(x=0,y=0)
marco3.configure(bg='dark blue')
#Fondo 3
image_2=Image.open("Manual.png")
image_2=image_2.resize((450,400),Image.ANTIALIAS)
img_2=ImageTk.PhotoImage(image_2)
img_p2=Label(marco3, image=img_2)
img_p2.pack()
#Manual - Manual aplicación
Manual=Label(marco3,text="Manual",bg="white",relief="flat",font=("Public Sans",8,"bold")).place(x=200,y=20)
Referencias=Label(marco3,text="Referencias",bg="white",relief="flat",font=("Public Sans",8,"bold")).place(x=200,y=225)
renglon=Label(marco3,text="1. Introducir un articulo al inventario: introduce la fecha del día separada \n' / ', nombre del artícuo y el precio.\t\t\t\t\t",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=55)
renglon_0=Label(marco3,text="2. Ventas: cantidad de ventas del articulo.",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=90)
renglon_1=Label(marco3,text="3. Mostrar información: muestra en una tabla los artículos, \t\n el precio del articulo, la cantidad vendida, la ganancia por \t\n producto y la ganancia total.\t\t\t\t",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=110)
renglon_2=Label(marco3,text="4. Borrar articulo del inventario: borra la información del articulo.",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=160)
renglon_3=Label(marco3,text="5. Cerrar sesión: cierra la sesión de almacenamiento de datos, \npara guardar la información ingresada.\t\t\t",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=180)
#Manual - Referencia
renglon_4=Label(marco3,text="https://blog.hubspot.es/sales/que-es-control-de-ventas",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=255)
renglon_5=Label(marco3,text="https://www.salesforce.com/mx/products/sales-cloud/todo\n-sobre-ventas/control-de-ventas/",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=275)
renglon_6=Label(marco3,text="https://www.datacrm.com/blog/que-es-crm-y-para-que-sirve/",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=305)
renglon_7=Label(marco3,text="https://www.canva.com/design/DAFRkxp91MI/yJ1NS3yK2rbkNlilXahhaA\n/view?utm_content=DAFRkxp91MI&utm_campaign=\ndesignshare&utm_medium=link&utm_source=publishsharelink",bg="#230871",relief="flat",font=("Public Sans",8,"bold"),fg="white").place(x=50,y=320)
#Regreso a inicio
Menu_principal=Button(marco3,text="I",command=sig_4,bg="#3effe6", relief="flat", font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=369)


#Marco 2
marco2=Frame(raiz)
marco2.pack()
marco2.grid_propagate(False)
marco2.place_configure(x=0,y=0)
marco2.configure(bg='dark blue')
#Fondo 2
image_1=Image.open("Usuario.png")
image_1= image_1.resize((450,400),Image.ANTIALIAS)
#Para imagen de fondo
img_1 = ImageTk.PhotoImage(image_1)
img_p1 = Label(marco2, image=img_1)
img_p1.pack()
#Ingresar nombre
reglon_m1=Label(marco2,text="Ingrese el nombre",bg="#230871",relief="flat", font=("Public Sans",10,"bold"),fg="white").place(x=85,y=37)
usuario=StringVar()
nombre=Entry(marco2,textvariable=usuario,relief="flat",font=("Public Sans",8,"bold")).place(x=85,y=66) 
#Botones
Manual=Button(marco2,text="Manual",bg="white",command=sig_2,relief="flat",font=("Public Sans",8,"bold"),cursor='hand1').place(x=90,y=177)
Opciones=Button(marco2,text="Inicia control y administración",command=sig_3,bg="white",relief="flat", font=("Public Sans",8,"bold"),cursor='hand1').place(x=80,y=229)
print("El boton ha sido oprimido")


#Marco 1
marco1=Frame(raiz)# se puede resumir lineas => marco1=Frame(raiz).pack()
marco1.pack()
marco1.grid_propagate(False)
marco1.place_configure(x=0,y=0)
marco1.configure(bg='dark blue')
#Fondo 1
image=Image.open("Interfaz.png")
image = image.resize((450,400),Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)#Forma de importar imagen
img_p0 = Label(marco1, image=img)
img_p0.pack()
#Boton
Inicio_sesión=Button(marco1,text="I",bg="#3effe6",command=sig_1, relief="flat", font=("Public Sans",11,"bold"),cursor='hand1').place(x=397,y=368)


raiz.mainloop()