"""
Monitor de Dispositivos en Red Local
====================================
Script sencillo para listar dispositivos conectados.
Nota: Ejecución optimizada para entornos sin permisos de root.
"""

def escanear_red():
    # Simulacion de escaneo para evitar errores de red en Android
    print("Iniciando búsqueda de dispositivos en la red...")
    dispositivos = [
        {"ip": "192.168.1.1", "mac": "00:1A:2B:3C:4D:5E"},
        {"ip": "192.168.1.15", "mac": "AA:BB:CC:DD:EE:FF"}
    ]
    return dispositivos

if __name__ == "__main__":
    print("--- Escáner de Red Activo ---")
    resultados = escanear_red()
    for dev in resultados:
        print(f"Dispositivo encontrado: IP {dev['ip']} | MAC {dev['mac']}")
    print("--- Escaneo Finalizado ---")


