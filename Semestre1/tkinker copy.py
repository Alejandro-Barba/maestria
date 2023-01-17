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
marco.config(width=480, height=320, cursor="dotbox")
#Ver tipos de cursores en https://www.tutorialspoint.com/python/tk_cursors.html

#Con la función pack le decimos que se empaquete dentro de su objeto padre
marco.pack()
#Probar con:
#y con:
#marco.pack(side='bottom', anchor="e")
#y con:
#marco.pack(fill='both', expand=1)

#Cambiamos el color de fondo del widget utilizando los colores de html
marco.config(bg="#fef5e7")
marco.config(bd=6)
marco.config(relief="ridge")

raiz.mainloop()