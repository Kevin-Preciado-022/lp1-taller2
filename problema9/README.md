# Problema 9: Sistema Distribuido (Coordinación entre servidores)

**Conceptos clave**:

- Múltiples servidores coordinados
- Balanceador de carga simple
- Replicación de datos
- Tolerancia a fallos básica

**Requerimientos**:

- Registro de servidores backend
- Health checks entre servidores
- Distribución de clientes
- Sincronización de datos

funciona de esta forma 
 ```bash
python3 backend.py 9101
```
en la terminal 1
```bash
python3 backend.py 9102
```
en 2 terminales diferentes

en otra terminal 
```bash
python3 balanceador.py
```

luego crea el clientes puedes escribir hola y en el mismo cliente se ve como guarda los mensajes

```bash
python3 cliente.py                                                  
```
Conectado al balanceador
Redirigido a ('localhost', 9102)
Bienvenido al servidor backend
hola 
Guardado: hola
