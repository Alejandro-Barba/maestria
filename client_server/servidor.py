import socket

#Creamos un socket nuevo 
primer_socket = socket.socket() 
print("El socket fue creado con éxito")

#Vinculando nuestra dirección IP y el número de puerto al socket
primer_socket.bind(('localhost', 8000)) #127.0.0.1
#localhost es la dirección del servidor y 8000 es el número de puerto a utilizar para la comunicación

print("El socket fué vinculado al puerto 8000")

#Le indicamos la cantidad de peticiones que puede manejar nuestro socket
primer_socket.listen(5)
print("El socket está preparado para recibir peticiones")

while True: 

    #Establecemos conexion con el cliente
    conexion, direccion = primer_socket.accept() #Retornamos la conexión y la dirección 
    print("Conexión establecida con éxito")


    datos="Hola! aquí tienes la información que necesitas"

    #Enviamos información al cliente
    conexion.send(datos.encode()) #Por defautl Python usa utf-8

    #Cerramos la conexión
    conexion.close()

    #Desconectamos la conexión para utilizar de nuevo la consola
    break
