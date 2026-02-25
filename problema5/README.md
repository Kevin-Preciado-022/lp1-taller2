# Problema 5: Transferencia de Archivos (Upload/Download)

**Conceptos clave**:

- Manejo de datos binarios
- Protocolo custom para transferencia de archivos
- Control de flujo y buffers
- Comandos: UPLOAD, DOWNLOAD, LIST


**Requerimientos**:

- Implementar protocolo de comandos
- Manejar archivos grandes con buffers
- Validar integridad de archivos (checksum)
- Manejo seguro de rutas de archivos

problema 5
Como funciona 
ingresa este codigo en la terminal 1

```bash
python3 servidor.py
```
Servidor escuchando en localhost:9001
Cliente conectado desde ('127.0.0.1', 58630)

luego en otra terminal 2

python3 cliente.py

debe aparecer este simbolo > y ingresas DOWNLOAD comando que agrega un archivo recien creado dentro de la carpeta problema 5

ejemplo de como se ve 

> UPLOAD prueba1.txt
Servidor: READY
Servidor: CHECKSUM=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
> DOWNLOAD prueba1.txt
Servidor: READY
#listo#
