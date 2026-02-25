# Problema 8: Servidor de Juegos (Estado compartido)

**Conceptos clave**:

- Juego Tic-Tac-Toe multijugador
- Estado compartido del juego
- Coordinación de turnos
- Notificaciones de eventos

**Requerimientos**:

- Estado del tablero de juego
- Matchmaking de jugadores
- Validación de movimientos
- Sistema de espectadores

funciona de esta forma

terminal 1

```bash
python3 juego.py 
```
Servidor de juegos en localhost:9002

terminal 2 
```bash
python3 cliente.py 
```
Bienvenido al servidor de Tic-Tac-Toe!
Eres jugador O

   |   |  
---+---+---
   |   |  
---+---+---
   |   |  
Tu movimiento (0-8): 

terminal 3
```bash
python3 cliente.py 
```
Bienvenido al servidor de Tic-Tac-Toe!
Eres jugador O

   |   |  
---+---+---
   |   |  
---+---+---
   |   |  
Tu movimiento (0-8):

la terminal 2 empieza primero al haber usado el python3 cliente.py primero  y si no se sigue el proceso 
Bienvenido al servidor de Tic-Tac-Toe!
Eres jugador O

   |   |  
---+---+---
   |   |  
---+---+---
   |   |  
Tu movimiento (0-8): 1
No es tu turno!
sucederá esto.