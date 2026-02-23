#!/usr/bin/env python3
import socket
import os

HOST = "localhost"
PORT = 9001
BUFFER_SIZE = 4096

def send_command(datos, Archivo=None):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    cliente.sendall(datos.encode())

    response = cliente.recv(BUFFER_SIZE).decode()
    print("Servidor:", response)

    if datos.startswith("UPLOAD") and response == "READY":
        with open(Archivo, "rb") as f:
            for chunk in iter(lambda: f.read(BUFFER_SIZE), b""):
                cliente.sendall(chunk)
        cliente.sendall(b"EOF")
        print("Servidor:", cliente.recv(BUFFER_SIZE).decode())

    elif datos.startswith("DOWNLOAD") and response == "READY":
        with open(Archivo, "wb") as f:
            while True:
                data = cliente.recv(BUFFER_SIZE)
                if data == b"EOF":
                    break
                f.write(data)
        # El servidor termina con EOF, no envía más mensajes

    elif datos.startswith("LIST"):
        print("Archivos disponibles:\n", response)

    cliente.close()


# --- 🔹 Bucle interactivo ---
while True:
    datos = input("> ")
    if datos.upper() == "EXIT":
        break
    if datos.startswith("UPLOAD"):
        _, Archivo = datos.split()
        send_command(datos, Archivo)
    elif datos.startswith("DOWNLOAD"):
        _, Archivo = datos.split()
        send_command(datos, Archivo)
    else:
        send_command(datos)
        
        
# --- 🔹 Ejemplo directo ---
send_command("DOWNLOAD prueba.txt", "descarga.txt")