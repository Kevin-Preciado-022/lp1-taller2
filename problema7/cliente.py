import socket

HOST = 'localhost'   # dirección del proxy
PORT = 8888          # puerto del proxy
BUFFER_SIZE = 4096

def main():
    # Crear socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    # Ejemplo de petición HTTP GET
    peticion = "GET http://example.com/ HTTP/1.1\r\nHost: example.com\r\n\r\n"
    cliente.sendall(peticion.encode())

    # Recibir respuesta del proxy (que viene del servidor destino)
    while True:
        datos = cliente.recv(BUFFER_SIZE)
        if not datos:
            break
        print(datos.decode(errors="ignore"), end="")

    cliente.close()

if __name__ == "__main__":
    main()
    #listo