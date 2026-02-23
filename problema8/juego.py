import socket
import threading

HOST = 'localhost'
PORT = 9002
BUFFER_SIZE = 1024

# Estado compartido del juego
board = [" "]*9
players = []
spectators = []
turn = 0
lock = threading.Lock()

def print_board():
    return f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]}
"""

def check_winner():
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "Empate"
    return None

def broadcast(msg):
    for p in players + spectators:
        try:
            p.sendall(msg.encode())
        except:
            pass

def handle_client(conn, addr):
    global turn
    conn.sendall("Bienvenido al servidor de Tic-Tac-Toe!\n".encode())

    with lock:
        if len(players) < 2:
            players.append(conn)
            symbol = "X" if len(players) == 1 else "O"
            conn.sendall(f"Eres jugador {symbol}\n".encode())
        else:
            spectators.append(conn)
            conn.sendall("Eres espectador. Observa el juego.\n".encode())
            conn.sendall(print_board().encode())
            return

    while True:
        try:
            conn.sendall(print_board().encode())
            conn.sendall("Tu movimiento (0-8): ".encode())
            move = conn.recv(BUFFER_SIZE).decode().strip()
            if not move:
                break

            with lock:
                if conn != players[turn]:
                    conn.sendall("No es tu turno!\n".encode())
                    continue

                if not move.isdigit() or int(move) not in range(9):
                    conn.sendall("Movimiento inválido!\n".encode())
                    continue

                move = int(move)
                if board[move] != " ":
                    conn.sendall("Casilla ocupada!\n".encode())
                    continue

                symbol = "X" if turn == 0 else "O"
                board[move] = symbol
                winner = check_winner()
                broadcast(print_board())

                if winner:
                    broadcast(f"Resultado: {winner}\n")
                    break

                turn = 1 - turn
        except:
            break

    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor de juegos en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
    #listo