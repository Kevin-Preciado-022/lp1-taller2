import socket
import threading

HOST = 'localhost'
PORT = 9001
BUFFER_SIZE = 1024

# Diccionario de salas: {"sala": set(sockets)}
salas = {}
# Diccionario de usuarios: {socket: nombre}
usuarios = {}

def broadcast(sala, mensaje, remitente=None):
    """Envía un mensaje a todos los usuarios de una sala"""
    for sock in salas.get(sala, []):
        if sock != remitente:
            sock.sendall(mensaje.encode())

def handle_client(conn, addr):
    conn.sendall("Bienvenido al servidor de chat. Ingresa tu nombre: ".encode())
    nombre = conn.recv(BUFFER_SIZE).decode().strip()
    usuarios[conn] = nombre
    conn.sendall(f"Hola {nombre}, usa comandos CREATE, JOIN, LEAVE, LIST, PRIVATE.\n".encode())

    while True:
        try:
            datos = conn.recv(BUFFER_SIZE).decode().strip()
            if not datos:
                break

            if datos.upper() == "EXIT":
                conn.sendall("Desconectado.\n".encode())
                break

            elif datos.startswith("CREATE"):
                _, sala = datos.split()
                if sala not in salas:
                    salas[sala] = set()
                    conn.sendall(f"Sala '{sala}' creada.\n".encode())
                else:
                    conn.sendall("La sala ya existe.\n".encode())

            elif datos.startswith("JOIN"):
                _, sala = datos.split()
                if sala in salas:
                    salas[sala].add(conn)
                    conn.sendall(f"Te uniste a la sala '{sala}'.\n".encode())
                    broadcast(sala, f"{usuarios[conn]} se unió a la sala.", conn)
                else:
                    conn.sendall("La sala no existe.\n".encode())

            elif datos.startswith("LEAVE"):
                _, sala = datos.split()
                if sala in salas and conn in salas[sala]:
                    salas[sala].remove(conn)
                    conn.sendall(f"Saliste de la sala '{sala}'.\n".encode())
                    broadcast(sala, f"{usuarios[conn]} salió de la sala.", conn)
                else:
                    conn.sendall("No estás en esa sala.\n".encode())

            elif datos.startswith("LIST salas"):
                conn.sendall(f"Salas disponibles: {', '.join(salas.keys())}\n".encode())

            elif datos.startswith("LIST usuarios"):
                _, _, sala = datos.split()
                if sala in salas:
                    nombres = [usuarios[s] for s in salas[sala]]
                    conn.sendall(f"Usuarios en '{sala}': {', '.join(nombres)}\n".encode())
                else:
                    conn.sendall("La sala no existe.\n".encode())

            elif datos.startswith("PRIVATE"):
                _, destinatario, mensaje = datos.split(" ", 2)
                for sock, nombre in usuarios.items():
                    if nombre == destinatario:
                        sock.sendall(f"[Privado de {usuarios[conn]}]: {mensaje}\n".encode())
                        conn.sendall("Mensaje privado enviado.\n".encode())
                        break
                else:
                    conn.sendall("Usuario no encontrado.\n".encode())

            else:
                # Mensaje normal: se envía a todas las salas donde esté el usuario
                for sala, miembros in salas.items():
                    if conn in miembros:
                        broadcast(sala, f"[{usuarios[conn]}]: {datos}", conn)

        except:
            break

    # Limpieza al desconectar
    for sala in salas.values():
        sala.discard(conn)
    usuarios.pop(conn, None)
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor de chat en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
    #listo