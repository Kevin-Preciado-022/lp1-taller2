import socket
import threading

BUFFER_SIZE = 1024

# Estado compartido simulado (replicación simple)
data_store = []

def handle_client(conn, addr):
    conn.sendall("Bienvenido al servidor backend\n".encode())
    while True:
        try:
            msg = conn.recv(BUFFER_SIZE).decode().strip()
            if not msg:
                break
            data_store.append(msg)
            conn.sendall(f"Guardado: {msg}\n".encode())
        except:
            break
    conn.close()

def main(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen(5)
    print(f"Backend escuchando en localhost:{port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9101
    main(port)