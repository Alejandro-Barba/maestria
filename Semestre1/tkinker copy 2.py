from tkinter import *  #Importamos todas las funciones que contiene tkinter

#Creamos el objeto que será la raiz de la aplicación
raiz = Tk()
#Le agregamos un título
raiz.title("Esta es mi Aplicación")
#Determinamos si se podrá cambiar su tamaño
raiz.resizable(1,1)
#Asignamos un logotipo
raiz.iconbitmap('objetos.ico')

#Asignamos un tipo de cursor, un color de background y un borde a la raiz
raiz.config(cursor="arrow")
raiz.config(bg="blue")
raiz.config(bd=8)
raiz.config(relief="ridge")


#Creamos un marco dentro de la raiz
marco = Frame(raiz)

#Le podemos indicar el tamaño que queremos que tenga
#y el tipo de cursor que queremos utilizar
marco.config(width=480, height=620, cursor="dotbox")
#Ver tipos de cursores en https://www.tutorialspoint.com/python/tk_cursors.htm

#Con la función pack le decimos que se empaquete dentro de su objeto padre
#marco.pack()
#Probar con:
#y con:
marco.pack(side='bottom', anchor="e")
#y con:
#marco.pack(fill='both', expand=1)

#Cambiamos el color de fondo del widget utilizando los colores de html
marco.config(bg="#fef5e7")
marco.config(bd=6)
marco.config(relief="ridge")

#Agregamos etiquetas al marco y a la raiz
etiqueta1 = Label(raiz, text="Esta es la base de mi aplicación")
etiqueta1.pack(anchor="nw")
etiqueta2 = Label(marco, text="Este es un marco")
etiqueta2.place(x=0, y=0)
etiqueta3 = Label(marco, text="Yo también estoy dentro del marco")
etiqueta3.place(x=50, y=50)

#Damos color, estilo y tamaño a las etiquetas
etiqueta1.config(bg="green", fg="white", font=("Verdana",24))

#Si queremos agregar una imágen lo hacemos como si se tratara de una etiqueta
#La función PhotoImage solo acepta los formato pgm y gif
imagen = PhotoImage(file="what.gif")
Label(raiz, image=imagen, bd=2).place(x=0, y=150)


#Para incluir imágenes de otros formatos utilizamos la librería PIL
from PIL import ImageTk, Image
#Cargamos la imágen
img = ImageTk.PhotoImage(Image.open("objetos.jpg"))

#Y la desplegamos
Label(raiz, image=img).place(x=0, y=350)


raiz.mainloop()