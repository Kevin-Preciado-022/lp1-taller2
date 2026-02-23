import socket 
import os
import hashlib

HOST = 'localhost'
PORT = 9001
BUFFER_SIZE = 1024
STORAGE = 'storage'

os.makedirs(STORAGE, exist_ok=True)

def safe_filename(filename):
    return os.path.join(STORAGE, os.path.basename(filename))

def checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(BUFFER_SIZE), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    cliente, direccion = servidor.accept()
    print(f"Cliente conectado desde {direccion}")
    
    datos = cliente.recv(BUFFER_SIZE).decode()
    parts = datos.split()
    if not parts:
        cliente.sendall(b"error:")
        cliente.close()
        continue
    cmd = parts[0].upper()
    
    if cmd == "LIST":
        files = os.listdir(STORAGE)
        response = "\n".join(files) if files else "No hay archivos disponibles."
        cliente.sendall(response.encode())
    elif cmd == "UPLOAD" and len(parts) == 2:
        Archivo = safe_filename(parts[1])
        if os.path.exists(Archivo):
            cliente.sendall(b"ERROR")
        else:
            cliente.sendall(b"READY")
            with open(Archivo, "wb") as f:
                while True:
                    datos =cliente.recv(BUFFER_SIZE)
                    if datos == b"EOF":
                        break
                    f.write(datos)
                    cliente.sendall(f"CHECKSUM={checksum(Archivo)}".encode())
                    
    elif cmd == "DOWNLOAD" and len(parts) == 2:
        Archivo = safe_filename(parts[1])
        if os.path.exists(Archivo):
            cliente.sendall(b"READY")
            with open(Archivo, "rb") as f:
                while True:
                    chunk = f.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    cliente.sendall(chunk)
            cliente.sendall(b"EOF")
        else:
            cliente.sendall(b"ERROR")
    else:
        cliente.sendall(b"ERROR")                    