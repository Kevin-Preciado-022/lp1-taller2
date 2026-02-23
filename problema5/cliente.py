#!/usr/bin/env python3
import socket
import os

HOST = "localhost"
PORT = 9001
BUFFER_SIZE = 4096

# Estructura básica del cliente
def send_command(datos, Archivo=None):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    cliente.sendall(datos.encode())

    response = cliente.recv(1024).decode()
    print("Servidor:", response)

    if datos.startswith("UPLOAD") and response == "READY":
        with open(Archivo, "rb") as f:
            for chunk in iter(lambda: f.read(BUFFER_SIZE), b""):
                cliente.sendall(chunk)
        cliente.sendall(b"EOF")
        print("Servidor:", cliente.recv(1024).decode())

    elif datos.startswith("DOWNLOAD") and response == "READY":
        with open(Archivo, "wb") as f:
            while True:
                data = cliente.recv(BUFFER_SIZE)
                if data == b"EOF":
                    break
                f.write(data)
        print("Servidor:", cliente.recv(1024).decode())

    elif datos.startswith("LIST"):
        print("Archivos disponibles:\n", response)

    cliente.close()

# Ejemplos de uso:
# send_command("UPLOAD prueba.txt", "prueba.txt")
# send_command("DOWNLOAD prueba.txt", "descarga.txt")
# send_command("LIST")
