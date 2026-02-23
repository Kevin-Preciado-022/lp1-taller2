import socket
import threading

HOST = 'localhost'
PORT = 9100   # Puerto del balanceador
BUFFER_SIZE = 1024

def recibir(sock):
    """Hilo para recibir mensajes del servidor/balanceador"""
    while True:
        try:
            data = sock.recv(BUFFER_SIZE).decode(errors="ignore")
            if not data:
                break
            print(data, end="")
        except:
            break

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    # Hilo para escuchar mensajes
    threading.Thread(target=recibir, args=(cliente,), daemon=True).start()

    # Bucle para enviar mensajes
    while True:
        try:
            entrada = input()
            if not entrada:
                continue
            cliente.sendall(entrada.encode())
            if entrada.upper() == "EXIT":
                break
        except KeyboardInterrupt:
            break
        except:
            break

    cliente.close()

if __name__ == "__main__":
    main()