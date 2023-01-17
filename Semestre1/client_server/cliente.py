import socket

#Creamos un socket nuevo
primer_socket = socket.socket()

#Vinculando nuestra dirección y el número de puerto al socket
primer_socket.connect(('localhost', 8000)) 
#localhost es la dirección del cliente y 8000 es el número de puerto a utilizar para la comunicación

#Recibimos y decodificamos la información enviada por el servidor
print(primer_socket.recv(1024).decode()) #1024 es la cantidad máxima de datos que pueden ser recibidos de una sola vez.

#Cerramos el socket
primer_socket.close()