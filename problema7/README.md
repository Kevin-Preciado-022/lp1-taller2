# Problema 7: Proxy HTTP (Intermediario de red)

**Conceptos clave**:

- Proxy transparente y explícito
- Reenvío de peticiones HTTP
- Modificación de headers
- Logging y monitoreo

**Requerimientos**:

- Recibir petición del cliente
- Conectar al servidor destino
- Reenviar datos bidireccional
- Manejar HTTPS (CONNECT method)

Como funciona ingresa este codigo en la terminal 1
```bash
python3 Proxy.py
```
debe ver eso 
python3 Proxy.py 
Proxy HTTP escuchando en localhost:8888
=== Petición recibida ===
GET http://example.com/ HTTP/1.1
=== Petición recibida ===
GET http://example.com/ HTTP/1.1

luego en otra terminal 


```bash
python3 cliente.py
```
Debe ver eso 
Date: Wed, 25 Feb 2026 00:43:50 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
CF-RAY: 9d332bb8cdb3e336-BOG
Last-Modified: Wed, 18 Feb 2026 05:34:44 GMT
Allow: GET, HEAD
Accept-Ranges: bytes
Age: 1601
cf-cache-status: HIT
Server: cloudflare

210
<!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>

0
#listo#