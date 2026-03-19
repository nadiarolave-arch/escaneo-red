import socket
from datetime import datetime

def escanear_ip(ip):
    # Intentamos conectar al puerto 80 (común en routers y dispositivos)
    # Si el puerto está cerrado pero el host existe, connect_ex suele dar error distinto a host no encontrado
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.05) # Tiempo de espera muy corto
    resultado = s.connect_ex((ip, 80))
    s.close()
    return resultado == 0

# Detectar tu IP local automáticamente
def obtener_mi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

mi_ip = obtener_mi_ip()
base_red = ".".join(mi_ip.split('.')[:-1])

print(f"--- Escaneando red: {base_red}.x ---")
print(f"Inicio: {datetime.now().strftime('%H:%M:%S')}\n")

for i in range(1, 255):
    ip_objetivo = f"{base_red}.{i}"
    if escanear_ip(ip_objetivo):
        print(f"[+] Dispositivo activo encontrado en: {ip_objetivo}")

print(f"\nEscaneo finalizado: {datetime.now().strftime('%H:%M:%S')}")





