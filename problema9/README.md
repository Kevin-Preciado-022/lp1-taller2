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
python3 backend.py 9101
python3 backend.py 9102
en 2 terminales diferentes

en otra terminal python3 balanceador.py

luego crea el clientes puedes escribir hola y en el mismo cliente se ve como guarda los mensajes

