# Problema 6: Chat con Salas (Gestión de grupos)

**Conceptos clave**:

- Gestión de múltiples salas/canales
- Estados de usuario más complejos
- Comandos avanzados de chat
- Sincronización de estado entre hilos

**Requerimientos**:

- Sistema de salas con JOIN, LEAVE, CREATE
- Lista de usuarios por sala
- Mensajes privados entre usuarios
- Persistencia básica de salas

Como funciona 

se ingresa esto en una terminal 
```bash
python3 servidor.py
```
Servidor de chat en localhost:9001

luego ingresa este cogido en terminal 2

```bash
python3 cliente.py
```
python3 cliente.py 
Bienvenido al servidor de chat. Ingresa tu nombre: > juan
Hola juan, usa comandos CREATE, JOIN, LEAVE, LIST, PRIVATE.
> CREATE mundo
Sala 'mundo' creada.
> JOIN mundo
Te uniste a la sala 'mundo'.
> LIST
Carlos se unió a la sala.> LIST
[Carlos]: LIST> PRIVATE Carlos Hola
Mensaje privado enviado.
> LIST
[Carlos]: LIST> 

luego ingresa este cogido en terminal 3

```bash
python3 cliente.py
```
Bienvenido al servidor de chat. Ingresa tu nombre: > Carlo
Hola Carlo, usa comandos CREATE, JOIN, LEAVE, LIST, PRIVATE.
> JOIN generales
Te uniste a la sala 'generales'.python3 cliente.py 
Bienvenido al servidor de chat. Ingresa tu nombre: > Carlos
Hola Carlos, usa comandos CREATE, JOIN, LEAVE, LIST, PRIVATE.
> JOIN mundo
Te uniste a la sala 'mundo'.
> PRIVATE juan Hola
Mensaje privado enviado.
> LIST
[juan]: LIST[juan]: LIST> LIST
[Privado de juan]: Hola
> 