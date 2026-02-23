import socket

HOST = 'localhost'
PORT = 9001
BUFFER_SIZE = 1024

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    while True:
        datos = cliente.recv(BUFFER_SIZE).decode()
        if datos:
            print(datos, end="")

        entrada = input("> ")
        cliente.sendall(entrada.encode())
        if entrada.upper() == "EXIT":
            break

    cliente.close()

if __name__ == "__main__":
    main()
    
    #listo