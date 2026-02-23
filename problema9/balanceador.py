import socket
import threading
import time

HOST = 'localhost'
PORT = 9100
BUFFER_SIZE = 1024

# Lista de servidores backend registrados
backends = [
    ("localhost", 9101),
    ("localhost", 9102)
]

# Estado de salud de cada backend
health = {backend: True for backend in backends}
index = 0
lock = threading.Lock()

def health_check():
    """Verifica periódicamente si los backends están vivos"""
    global health
    while True:
        for backend in backends:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect(backend)
                s.close()
                health[backend] = True
            except:
                health[backend] = False
        time.sleep(3)

def handle_client(conn, addr):
    global index
    conn.sendall("Conectado al balanceador\n".encode())

    with lock:
        # Selección simple round-robin
        available = [b for b in backends if health[b]]
        if not available:
            conn.sendall("No hay servidores disponibles\n".encode())
            conn.close()
            return
        backend = available[index % len(available)]
        index += 1

    try:
        # Redirigir petición al backend elegido
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(backend)
        conn.sendall(f"Redirigido a {backend}\n".encode())

        # Forward bidireccional
        threading.Thread(target=forward, args=(conn, s)).start()
        threading.Thread(target=forward, args=(s, conn)).start()
    except Exception as e:
        conn.sendall(f"Error al conectar con backend: {e}\n".encode())
        conn.close()

def forward(src, dst):
    while True:
        try:
            data = src.recv(BUFFER_SIZE)
            if not data:
                break
            dst.sendall(data)
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Balanceador escuchando en {HOST}:{PORT}")

    threading.Thread(target=health_check, daemon=True).start()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()