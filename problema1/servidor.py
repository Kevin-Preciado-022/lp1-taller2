#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - servidor.l
Objetivo: Crear un servidor TCP que acepte una conexión y intercambie mensajes básicos
"""

import socket

# : Definir la dirección y puerto del servidor
HOST ='Localhost'
PORT = 9001
# : Crear un socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)

# : Enlazar el socket a la dirección y puerto especificados

# : Poner el socket en modo escucha
# El parámetro define el número máximo de conexiones en cola
print("servidor a la espera de conexiones ...")

# : Aceptar una conexión entrante
cliente, direccion = servidor.accept()
print(f"un cliente se conecto desde la direccion ", direccion)

datos = cliente.recv(1024)
cliente.sendall(b"Hola! " + datos) # ojo! debe ser binario, no cadena 
cliente.close()
# accept() bloquea hasta que llega una conexión
# conn: nuevo socket para comunicarse con el cliente

# addr: dirección y puerto del cliente

print(f"Conexión realizada por {direccion}")

# : Recibir datos del cliente (hasta 1024 bytes)
 
# : Enviar respuesta al cliente (convertida a bytes)
# sendall() asegura que todos los datos sean enviados

# : Cerrar la conexión con el cliente

