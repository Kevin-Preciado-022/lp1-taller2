import socket
import threading

HOST = 'localhost'
PORT = 8888
BUFFER_SIZE = 4096

def handle_client(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode(errors="ignore")
    if not request:
        client_socket.close()
        return

    # Logging básico
    print("=== Petición recibida ===")
    print(request.split("\r\n")[0])  # primera línea (método y URL)

    # Manejo de HTTPS (CONNECT)
    if request.startswith("CONNECT"):
        host_port = request.split()[1]
        host, port = host_port.split(":")
        port = int(port)

        # Conectar al servidor destino
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote.connect((host, port))
        client_socket.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")

        # Reenvío bidireccional
        forward(client_socket, remote)
        return

    # Manejo de HTTP normal
    try:
        # Extraer host del header
        lines = request.split("\r\n")
        host_line = [h for h in lines if h.lower().startswith("host:")][0]
        host = host_line.split()[1]
        port = 80

        # Conectar al servidor destino
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote.connect((host, port))
        remote.sendall(request.encode())

        # Reenvío de respuesta
        while True:
            data = remote.recv(BUFFER_SIZE)
            if not data:
                break
            client_socket.sendall(data)

        remote.close()
        client_socket.close()
    except Exception as e:
        print("Error:", e)
        client_socket.close()

def forward(source, destination):
    """Reenvío bidireccional entre cliente y servidor destino"""
    def pipe(src, dst):
        while True:
            data = src.recv(BUFFER_SIZE)
            if not data:
                break
            dst.sendall(data)

    threading.Thread(target=pipe, args=(source, destination)).start()
    threading.Thread(target=pipe, args=(destination, source)).start()

def main():
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy.bind((HOST, PORT))
    proxy.listen(100)
    print(f"Proxy HTTP escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = proxy.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
    #listo